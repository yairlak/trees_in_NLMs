


def hebrew_lexicon():
    lexicon = {}

    # THIS
    lexicon['this'] = {}
    lexicon['this']['singular'] = {}
    lexicon['this']['plural'] = {}
    lexicon['this']['singular']['masculine'] = 'זה'
    lexicon['this']['singular']['feminine'] = 'זו'
    lexicon['this']['plural']['masculine'] = 'אלו'
    lexicon['this']['plural']['feminine'] = 'אלו'

    # WHICH
    lexicon['which'] = {}
    lexicon['which']['singular'] = {}
    lexicon['which']['plural'] = {}
    lexicon['which']['singular']['masculine'] = 'איזה'
    lexicon['which']['singular']['feminine'] = 'איזו'
    lexicon['which']['plural']['masculine'] = 'אילו'
    lexicon['which']['plural']['feminine'] = 'אילו'

    # NOUNS
    lexicon['nouns'] = {}

    lexicon['nouns']['humans'] = {}
    lexicon['nouns']['humans']['singular'] = {}
    lexicon['nouns']['humans']['plural'] = {}

    lexicon['nouns']['humans']['singular']['masculine'] = ['ילד','איש', 'שוטר', 'רופא']
    lexicon['nouns']['humans']['singular']['feminine'] = ['ילדה','אישה', 'שוטרת', 'רופאה']
    lexicon['nouns']['humans']['plural']['masculine'] = ['ילדים','אנשים', 'שוטרים', 'רופאים']
    lexicon['nouns']['humans']['plural']['feminine'] = ['ילדות','נשים', 'שוטרות', 'רופאות']

    lexicon['nouns']['objects'] = {}
    lexicon['nouns']['objects']['singular'] = {}
    lexicon['nouns']['objects']['plural'] = {}

    lexicon['nouns']['objects']['singular']['masculine'] = ['מזלג','סכין', 'מקל']
    lexicon['nouns']['objects']['singular']['feminine'] = ['כוס','צלחת', 'בובה']
    lexicon['nouns']['objects']['plural']['masculine'] = ['מזלגות','סכינים', 'מקלות']
    lexicon['nouns']['objects']['plural']['feminine'] = ['כוסות','צלחות', 'בובות']

    # VERBS
    lexicon['verbs'] = {}

    # transitive
    lexicon['verbs']['transitive'] = {}
    lexicon['verbs']['transitive']['humans'] = {}
    lexicon['verbs']['transitive']['humans']['singular'] = {}
    lexicon['verbs']['transitive']['humans']['plural'] = {}

    lexicon['verbs']['transitive']['humans']['singular']['masculine'] = ['פגש','ראה', 'חיפש']
    lexicon['verbs']['transitive']['humans']['singular']['feminine'] = ['פגשה','ראתה', 'חיפשה']
    lexicon['verbs']['transitive']['humans']['plural']['masculine'] = ['פגשו','ראו', 'חיפשו']
    lexicon['verbs']['transitive']['humans']['plural']['feminine'] = ['פגשו','ראו', 'חיפשו']

    # unaccusative
    lexicon['verbs']['unaccusative'] = {}
    lexicon['verbs']['unaccusative']['humans'] = {}
    lexicon['verbs']['unaccusative']['objects'] = {}
    lexicon['verbs']['unaccusative']['humans']['singular'] = {}
    lexicon['verbs']['unaccusative']['humans']['plural'] = {}
    lexicon['verbs']['unaccusative']['objects']['singular'] = {}
    lexicon['verbs']['unaccusative']['objects']['plural'] = {}

    lexicon['verbs']['unaccusative']['humans']['singular']['masculine'] = ['נפל','נעלם']
    lexicon['verbs']['unaccusative']['humans']['singular']['feminine'] = ['נפלה','נעלמה']
    lexicon['verbs']['unaccusative']['humans']['plural']['masculine'] = ['נפלו','נעלמו']
    lexicon['verbs']['unaccusative']['humans']['plural']['feminine'] = ['נפלו','נעלמו']

    lexicon['verbs']['unaccusative']['objects']['singular']['masculine'] = ['נשבר', 'נעלם']
    lexicon['verbs']['unaccusative']['objects']['singular']['feminine'] = ['נשברה', 'נעלמה']
    lexicon['verbs']['unaccusative']['objects']['plural']['masculine'] = ['נשברו', 'נעלמו']
    lexicon['verbs']['unaccusative']['objects']['plural']['feminine'] = ['נשברו', 'נעלמו']

    # unergative
    lexicon['verbs']['unergative'] = {}
    lexicon['verbs']['unergative']['humans'] = {}
    lexicon['verbs']['unergative']['objects'] = {}
    lexicon['verbs']['unergative']['humans']['singular'] = {}
    lexicon['verbs']['unergative']['humans']['plural'] = {}
    lexicon['verbs']['unergative']['objects']['singular'] = {}
    lexicon['verbs']['unergative']['objects']['plural'] = {}

    lexicon['verbs']['unergative']['humans']['singular']['masculine'] = ['ישן','קפץ','אכל']
    lexicon['verbs']['unergative']['humans']['singular']['feminine'] = ['ישנה','קפצה','אכלה']
    lexicon['verbs']['unergative']['humans']['plural']['masculine'] = ['ישנו','קפצו','אכלו']
    lexicon['verbs']['unergative']['humans']['plural']['feminine'] = ['ישנו','קפצו','אכלו']

    lexicon['verbs']['unergative']['objects']['singular']['masculine'] = []
    lexicon['verbs']['unergative']['objects']['singular']['feminine'] = []
    lexicon['verbs']['unergative']['objects']['plural']['masculine'] = []
    lexicon['verbs']['unergative']['objects']['plural']['feminine'] = []

    lexicon['places'] = ['גן', 'גינה', 'בית', 'מטבח']

    return lexicon

