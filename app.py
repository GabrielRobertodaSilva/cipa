from flask import Flask, render_template, request, session, redirect

app = Flask(__name__)
app.secret_key = 'chave_secreta_para_o_jogo'


jogo = {

    "fase1":{

        "pergunta": "Qual é o significado da sigla CIPA ?",

        "opcao":{
            "A": "Comissão interna de Prevenção a Acidentes e Assedio",
            "B": "Comssião interna de prevenção a Acidentes"
        },
        "correta": "A"
    },

    "fase2":{
        "pergunta": "Para qual número devo ligar se uma pessoa do meu trabalho passar mal ?",

        "opcao":{
            "B": "192",
            "A": "193"
        },
        "correta": "B"
    }
}








@app.route('/')

def index():
    return render_template('index.html')


@app.route('/jogo')

def tela_jogo():

    if 'fase_atual' not in session:
        session['fase_atual']= 'fase1'
        session['pontos']=0
    fase = session['fase_atual']


    if fase not in jogo:
        pontos_finais = session.get('pontos', 0)
        session.clear()
        return render_template('feedback.html', pontos=pontos_finais)

    
    dados_da_fase = jogo[fase]
    return render_template('jogo.html', dados=dados_da_fase, pontos=session['pontos'])

@app.route('/responder', methods=['POST'])
def responder():
    resp_usuario = request.form.get('resposta_usuario', '').strip().upper()
    fase = session.get('fase_atual', 'fase1')

    dados_da_fase = jogo[fase]

    # Valida a resposta do usuário
    if resp_usuario == dados_da_fase["correta"]:
        session['pontos'] += 1
        
   

    # Avança para a próxima fase mudando o número (ex: fase1 -> fase2)
    # Pegamos o número atual e somamos 1
    numero_fase_atual = int(fase.replace('fase', ''))
    session['fase_atual'] = f"fase{numero_fase_atual + 1}"
        
    return redirect('/jogo')


if __name__ == '__main__':
    app.run(debug=True)

        
    
   

        

