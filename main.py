from flask import Flask, request, send_file, render_template
import pandas as pd
import numpy as np
import io

app = Flask(__name__)

# Conversion functions
def decimal_to_logmar(decimal_va):
    """ Convert decimal visual acuity to LogMAR. """
    try:
        if decimal_va < 0:
            return None
        return round(-np.log10(decimal_va), 2)
    except ValueError:
        return None

def logmar_to_vas(logmar_va):
    """ Convert LogMAR visual acuity to Visual Analog Scale (VAS). """
    try:
        return round(100 - (50 * logmar_va), 2)
    except ValueError:
        return None

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/convert', methods=['POST'])
def upload_file():
    try:
        if 'file' not in request.files:
            return "No file part"
        
        file = request.files['file']
        if file.filename == '':
            return "No selected file"
        
        format_type = request.form.get('format', 'decimal')
        columns = request.form.get('columns', '').split(',')
        columns = [col.strip() for col in columns]  # Clean up any extra spaces

        if file and file.filename.endswith(('.xlsx', '.xls')):
            df = pd.read_excel(file)
            
            # Check if specified columns exist in the DataFrame
            missing_cols = [col for col in columns if col not in df.columns]
            if missing_cols:
                return f"Missing columns in the dataset: {', '.join(missing_cols)}"

            # Apply conversion functions based on the selected format
            if format_type == 'decimal':
                # Convert Decimal to LogMAR and add new columns for LogMAR
                df[[f'{col}_logmar' for col in columns]] = df[columns].applymap(decimal_to_logmar)
                
                # Convert LogMAR to VAS and add new columns for VAS
                df[[f'{col}_vas' for col in columns]] = df[[f'{col}_logmar' for col in columns]].applymap(logmar_to_vas)
                
            elif format_type == 'logmar':
                # Convert LogMAR to VAS directly
                df[[f'{col}_vas' for col in columns]] = df[columns].applymap(logmar_to_vas)
            else:
                return "Invalid format type selected."

            # Save the transformed DataFrame to a bytes buffer
            output = io.BytesIO()
            df.to_excel(output, index=False, engine='openpyxl')
            output.seek(0)

            return send_file(output, as_attachment=True, download_name='Converted_data.xlsx', mimetype='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
        
        return "Invalid file type. Please upload an Excel file."
    except Exception as e:
        app.logger.error(f"An error occurred: {e}")
        return f"An error occurred: {e}"

if __name__ == '__main__':
    app.run(debug=True)
