import re

usuario = {
    "nome": None,
    "idade": None
}

print("Bot: Olá! Vamos conversar 😊")
print("Bot: Primeiro, me diga seu nome.")

# -----------------------------
# LOOP PRINCIPAL
# -----------------------------
while True:
    msg = input("Você: ").lower().strip()

    if msg == "sair":
        print("Bot: Até mais!")
        break

    # -------------------------
    # NOME
    # -------------------------
    if "meu nome é" in msg:
        usuario["nome"] = msg.replace("meu nome é", "").strip().capitalize()
        print(f"Bot: Prazer em te conhecer, {usuario['nome']}!")
        continue

    # -------------------------
    # IDADE (TODOS OS CASOS)
    # -------------------------
    if "minha idade é" in msg or "tenho" in msg:
        numeros = re.findall(r"\d+", msg)
        if numeros:
            usuario["idade"] = int(numeros[0])
            print(f"Bot: Entendi! Você tem {usuario['idade']} anos.")
        else:
            print("Bot: Não consegui entender sua idade.")
        continue

    if msg.isdigit():
        usuario["idade"] = int(msg)
        print(f"Bot: Entendi! Você tem {usuario['idade']} anos.")
        continue

    # -------------------------
    # PERGUNTAS (mais flexível)
    # -------------------------
    if "nome" in msg:
        if usuario["nome"]:
            print(f"Bot: Seu nome é {usuario['nome']}.")
        else:
            print("Bot: Ainda não sei seu nome.")
        continue

    if "idade" in msg:
        if usuario["idade"]:
            print(f"Bot: Você tem {usuario['idade']} anos.")
        else:
            print("Bot: Ainda não sei sua idade.")
        continue

    # -------------------------
    # SAUDAÇÕES
    # -------------------------
    if "oi" in msg or "olá" in msg:
        nome = usuario["nome"] if usuario["nome"] else "você"
        print(f"Bot: Oi {nome}!")
        continue

    if "tudo bem" in msg or "como vai" in msg:
        print("Bot: Estou ótimo!")
        continue

    # -------------------------
    # RESPOSTA PADRÃO (ÚLTIMO CASO)
    # -------------------------
    print("Bot: Entendi... me conta mais.")