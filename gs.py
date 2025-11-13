# =====================================================================
# Projeto: Monitoramento de Bem-Estar e Requalificação Profissional
# Integrantes:
# - Nome: Josué Faria da Silva – RM: 563819
# - Nome: Julia Schiavi – RM: 562418
# =====================================================================

# Função que avalia o risco de burnout com base em estresse, sono e atividade física
def avaliar_bem_estar(estresse, sono, atividade):
# Verifica alto risco: estresse alto e pouco sono
    if estresse >= 7 and sono < 6:
        return "ALTO"
# Verifica risco médio: estresse moderado ou sono insuficiente
    elif estresse >= 5 or sono < 7:
        return "MÉDIO"
# Caso contrário, risco baixo    
    else:
        return "BAIXO"
    
def recomendar_acoes(risco):

    if risco == "ALTO":
        acoes = ["Agendar consulta psicológica", "Reduzir carga horária temporariamente"]
        cursos = ["Gestão do Estresse", "Equilíbrio entre vida pessoal e trabalho"]

    elif risco == "MÉDIO":
        acoes = ["Fazer pausas durante o expediente", "Praticar atividade física leve"]
        cursos = ["Mindfulness", "Inteligência emocional no trabalho"]

    else:
        acoes = ["Manter hábitos saudáveis", "Continuar rotina equilibrada"]
        cursos = ["Aprendizado Contínuo", "Autogestão de Carreira"]
    return acoes, cursos