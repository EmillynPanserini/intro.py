import os
from dotenv import load_dotenv
from openai import OpenAI

# Carrega as variáveis do arquivo .env
load_dotenv()

# Configura o cliente OpenAI com a chave de API carregada do .env
client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)
# Ler o conteúdo do arquivo .txt
with open('conversa.txt', 'r', encoding='utf-8') as file:
    conversa_teste = file.read()

# Função para analisar uma conversa
def analisar_conversa(conversa):
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",  # ou o modelo mais recente disponível
        messages=[
            {
                "role": "user",
                "content": f"""
                Avalie a seguinte troca de mensagens entre um cliente e um atendente:

                {conversa}

                Leve em consideração todos os aspectos da conversa, especialmente o comportamento profissional do atendente. Qualquer comportamento inadequado, como insultos, linguagem ofensiva ou falta de profissionalismo, deve resultar em uma nota muito baixa, independentemente do resto da interação.

                Forneça uma avaliação para os seguintes critérios, no formato JSON:
                {{
                    "Qualidade do atendimento": (um número de 1 a 10),
                    "Satisfação do usuário": (um número de 1 a 10),
                    "Nota geral do atendimento": (um número de 1 a 10),
                    "Profissionalismo do atendimento": (um número de 1 a 10),
                    "Motivo geral das notas": "breve descrição explicando as notas, com foco em comportamentos inadequados"
                }}

                Siga estritamente o formato JSON. Não adicione texto fora da estrutura JSON.
                """
            }
        ],
        temperature=0.2,  # Reduzindo ainda mais a variação criativa
        max_tokens=250,
    )
    return response.choices[0].message.content.strip()

# Teste da função com a conversa lida do arquivo
resultado = analisar_conversa(conversa_teste)
print(resultado)