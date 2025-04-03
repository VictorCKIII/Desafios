from flask import Flask, request, jsonify
import pandas as pd
from fuzzywuzzy import fuzz
from flask_cors import CORS
app = Flask(__name__)
CORS(app)


df = pd.read_csv('Relatorio_cadop.csv' , encoding='utf-8', delimiter=';')
df.to_csv('Relatorio_formatado.csv', encoding='utf-8-sig', index= False, sep=';')

csv_path = 'Relatorio_formatado.csv'

# df_csv = pd.read_csv(csv_path, encoding='utf-8-sig', sep=';')

df = pd.read_csv(csv_path, usecols=['Razao_Social', 'Nome_Fantasia'], encoding='utf-8-sig', sep=';')

@app.route('/buscar', methods=['GET'])
def buscar():
    termo = request.args.get('q', '').lower()
    print("✅ Requisição recebida! Parâmetros:", request.args)
    
    if not termo:
        return jsonify({"error": "Forneça um termo de busca"}), 400
    
    try:
        resultados = df[
            df['Razao_Social'].str.lower().str.contains(termo, na=False) | 
            df['Nome_Fantasia'].str.lower().str.contains(termo, na=False)
        ]
        
        # Substitui NaN por None (que vira null no JSON)
        resultados = resultados.where(pd.notnull(df), None)
        
        # Converte para dicionário garantindo tratamento adequado
        return jsonify(resultados.to_dict(orient='records'))
        
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    

if __name__ == '__main__':
    app.run(debug=True)
