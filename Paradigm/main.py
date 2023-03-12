import pytholog as pl


def main():
    knowledge_base = pl.KnowledgeBase("Game")
    knowledge_base([
        "Зайти на(Игрок, Конкретный персонаж)",
        "Создать(Игрок, Аккаунт)",
        "Выбрать(Игрок, Расса)",
        "Выбрать(Игрок, Класс)",
        "Авторизоваться в(Игрок, Игра) :- Создать(Игрок, Аккаунт)",
        "Создать(Игрок, Персонаж) :- Выбрать(Игрок, Расса)",
        "Создать(Subj, Obj) :- Выбрать(Игрок, Класс)",
        "Выбрать(Игрок, Конкретный персонаж)"
    ])
    
    print(knowledge_base.query(pl.Expr("Зайти на(Who, Конкретный персонаж)")))
    print(knowledge_base.query(pl.Expr("Создать(Subj, Obj)")))

if __name__ == "__main__":
    main()