import json
import os

# Resolve the data file relative to this script (304/scripts/ -> 304/data/)
OPEN_QUESTIONS_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "data", "open_questions.json")

with open(OPEN_QUESTIONS_PATH, "r", encoding="utf-8") as f:
    questions = json.load(f)

model_answers = {
    "OPEN-1": (
        "La psychologie clinique et la psychopathologie d'orientation psychanalytique reposent sur plusieurs principes éthiques fondamentaux :\n"
        "1. Le respect de la singularité du sujet : chaque patient est appréhendé dans son histoire propre et sa réalité psychique subjective, au-delà de toute catégorisation normative ou statistique.\n"
        "2. La neutralité bienveillante : le clinicien accueille la parole du patient sans porter de jugement moral, de conseil directif ou de censure idéologique.\n"
        "3. La règle d'abstinence : le praticien refuse toute satisfaction directe des demandes pulsionnelles, affectives ou séductrices, maintenant un cadre protecteur propice au travail d'élaboration psychique et à l'analyse du transfert.\n"
        "4. Le respect de l'association libre : le sujet chemine par la parole à son propre rythme dans un cadre d'écoute non directive.\n"
        "5. Le secret professionnel absolu : il garantit la confidentialité indispensable à l'alliance thérapeutique et préserve l'intimité du matériel psychique confié."
    ),
    "OPEN-2": (
        "En psychopathologie d'orientation psychanalytique, le principal symptôme de la pathologie névrotique est l'angoisse. "
        "Cette angoisse traduit un conflit intrapsychique non résolu entre les exigences pulsionnelles du Ça et les interdits du Surmoi, arbitré douloureusement par le Moi. Chez le névrosé, elle s'organise autour de l'angoisse de castration issue de la problématique œdipienne.\n\n"
        "Face à ce débordement de l'angoisse, on distingue deux grandes dérives symptomatiques :\n"
        "1. La dérive par repli ou évitement (phobique et hystérique) : l'angoisse est déplacée sur un objet ou une situation externe (phobie), conduisant à des conduites d'évitement protectrices ; ou bien elle est convertie dans le corps somatique (hystérie de conversion), où le symptôme corporel exprime symboliquement le conflit refoulé.\n"
        "2. La dérive par activisme ou lutte compulsive (obsessionnelle) : le sujet tente de maîtriser l'angoisse par une intense activité mentale défensive (doutes, ruminations) et des rituels conjuratoires répétitifs (compulsions), mobilisant l'isolation de l'affect et l'annulation rétroactive."
    ),
    "OPEN-3": (
        "L'entretien anamnestique a pour objectif fondamental de retracer l'histoire du sujet et la chronologie d'apparition de ses troubles afin de situer la souffrance actuelle dans sa trajectoire développementale et biographique globale. Il vise à recueillir les antécédents personnels et familiaux, les étapes du développement psychomoteur et affectif, les événements de vie stressants ou traumatiques, ainsi que l'évolution temporelle des symptômes.\n\n"
        "Dans le cadre d'une approche multidimensionnelle, son importance est majeure à plusieurs titres :\n"
        "1. Articulation bio-psycho-sociale : il évite le réductionnisme en croisant les facteurs biologiques (vulnérabilités somatiques/génétiques), psychologiques (personnalité, mécanismes de défense, représentations) et environnementaux (dynamique familiale, réseau de soutien).\n"
        "2. Identification de la dynamique diathèse-stress : il met en lumière les facteurs prédisposants anciens et les facteurs déclenchants actuels, tout en repérant les facteurs de protection (résilience).\n"
        "3. Compréhension du sens singulier : il permet d'élucider la signification subjective du trouble dans l'histoire de la personne et constitue le socle indispensable d'une alliance thérapeutique solide."
    ),
    "OPEN-4": (
        "Dans le cadre de l'approche bio-psycho-sociale (Engel), l'intérêt de l'entretien anamnestique est d'appréhender le fonctionnement du sujet à travers l'interaction dynamique de trois dimensions interdépendantes :\n"
        "- Dimension biologique : repérage des antécédents médicaux, familiaux et des vulnérabilités neuro-développementales.\n"
        "- Dimension psychologique : exploration des étapes du développement affectif, des schémas d'attachement, des processus de défense et du sens subjectif attribué aux épreuves de vie.\n"
        "- Dimension sociale : analyse du contexte familial, des relations interpersonnelles, de l'insertion professionnelle et des stresseurs environnementaux.\n"
        "L'anamnèse permet ainsi d'éviter tout réductionnisme (médicalisant ou purement intrapsychique). Elle permet d'identifier l'articulation singulière entre les facteurs de risque et les facteurs de protection mobilisables, offrant une base cohérente pour un projet thérapeutique global et individualisé."
    ),
    "OPEN-5": (
        "Le manuel diagnostique et statistique des troubles mentaux (DSM) s'appuie sur une démarche critériologique standardisée reposant sur quatre types de critères fondamentaux :\n"
        "1. Critères symptomatiques (ou d'inclusion) : liste sémiologique de signes et symptômes cliniques observables, dont un nombre minimal (seuil diagnostique) doit obligatoirement être présent.\n"
        "2. Critère temporel (ou d'évolution) : durée minimale exigée pour la présence des symptômes (ex: au moins 2 semaines pour l'épisode dépressif, 6 mois pour la schizophrénie).\n"
        "3. Critère de retentissement fonctionnel (ou détresse clinique) : altération cliniquement significative du fonctionnement personnel, social, familial ou professionnel du sujet.\n"
        "4. Critères d'exclusion différentielle : vérification que les troubles ne sont pas imputables aux effets physiologiques d'une substance (médicament, toxique) ni à une affection médicale générale, et qu'ils ne sont pas mieux expliqués par une autre pathologie mentale."
    ),
    "OPEN-6": (
        "1. Définitions (6 points) :\n"
        "- Facteurs de risque : caractéristiques biologiques (vulnérabilité génétique), psychologiques (impulsivité, cognitions négatives) ou environnementales (maltraitance, précarité, isolement) qui augmentent statistiquement la probabilité qu'un individu développe ou aggrave un trouble psychopathologique.\n"
        "- Facteurs de protection : ressources internes (estime de soi, compétences de régulation émotionnelle) ou contextuelles (entourage soutenant, adulte référent / tuteur de résilience) qui modèrent, neutralisent ou compensent l'impact négatif des facteurs de risque.\n\n"
        "2. Intégration dans une approche multidimensionnelle (6 points) :\n"
        "L'approche multidimensionnelle intègre ces facteurs à travers le modèle diathèse-stress et la psychopathologie développementale (Sroufe) :\n"
        "- Interaction non-linéaire : le trouble ne provient jamais d'une cause isolée mais de la rencontre entre une vulnérabilité interne et des stresseurs externes.\n"
        "- Principes d'équifinalité et de multifinalité : plusieurs combinaisons de risques peuvent conduire à un trouble identique (équifinalité), tandis qu'un même risque peut déboucher sur des trajectoires différentes selon les facteurs de protection disponibles (multifinalité).\n"
        "- Balance adaptative : la pathologie se manifeste lorsque la charge cumulative des risques submerge les capacités d'absorption des facteurs de protection."
    ),
    "OPEN-7": (
        "Pour identifier les facteurs de risque et de protection, le psychologue dispose de plusieurs techniques cliniques complémentaires :\n"
        "1. L'entretien clinique semi-structuré ou libre : exploration minutieuse de l'histoire de vie, de l'anamnèse et des représentations subjectives. Exemple : recherche d'antécédents de ruptures précoces et repérage de figures d'attachement sécurisantes.\n"
        "2. Les échelles et questionnaires psychométriques standardisés : mesure quantitative de dimensions spécifiques. Exemple : évaluation du niveau anxio-dépressif (BDI, STAI) ou du soutien social perçu (échelle SSQ de Sarason).\n"
        "3. Le génogramme familial : cartographie graphique des liens et transmissions intergénérationnelles sur 3 générations. Exemple : identification de deuils non élaborés ou d'alliances protectrices familiales.\n"
        "4. Les épreuves projectives (Rorschach, TAT) : analyse de la dynamique défensive profonde et de l'angoisse sous-jacente.\n"
        "5. L'observation clinique directe et les entretiens avec l'entourage : évaluation des interactions réelles et du climat familial."
    ),
    "OPEN-8": (
        "En métapsychologie psychanalytique, le point de vue topique (du grec topos, lieu) renvoie à une spatialisation conceptuelle de l'appareil psychique. Il postule que la psyché est constituée de plusieurs systèmes ou lieux psychiques différenciés, disposant chacun de fonctions, de contenus et de lois de fonctionnement propres.\n\n"
        "La 1re topique freudienne (1900-1915) comprend trois systèmes articulés par des censures :\n"
        "1. Le système Inconscient (Ics) : réservoir des désirs et représentations de choses refoulées. Il est soumis au processus primaire (énergie libre, condensation, déplacement, absence de doute et de contradiction temporelle) et gouverné par le principe de plaisir.\n"
        "2. Le système Préconscient (Pcs) : constitué de représentations de mots accessibles à la conscience par un effort d'attention. Il fonctionne selon le processus secondaire (énergie liée, logique formelle, principe de réalité).\n"
        "3. Le système Conscient (Cs) : organe récepteur situé à la périphérie du psychisme recevant les informations du monde extérieur (perceptions) et intérieur (sensations de plaisir/déplaisir)."
    ),
    "OPEN-9": (
        "La dissociation (terme de Bleuler : Spaltung) ou discordance (terme de Chaslin) désigne le syndrome fondamental de la schizophrénie. Elle correspond à la perte de cohésion et d'harmonie entre les différents registres de la vie psychique (pensée, affectivité, comportement).\n\n"
        "Elle se décline dans trois dimensions cliniques :\n"
        "1. Dimension intellectuelle (cours de la pensée) : dislocation de la pensée logique, diffluence, altération de l'attention. Exemple : le barrage (interruption brutale et involontaire du discours au milieu d'une phrase) ou l'usage de néologismes incompréhensibles.\n"
        "2. Dimension affective : rupture entre l'émotion manifestée et le contenu des représentations, ambivalence affective. Exemple : la paratémie ou rire immotivé (le patient sourit en racontant le décès tragique d'un proche).\n"
        "3. Dimension motrice / comportementale : incohérence gestuelle, bizarreries posturales. Exemple : le maniérisme gestuel, les stéréotypies ou le négativisme catatonique (maintien d'une posture figée avec opposition à toute mobilisation)."
    ),
    "OPEN-10": (
        "Définition : La psychoéducation est une démarche pédagogique et thérapeutique structurée visant à transmettre au patient et à ses proches des compétences et des connaissances scientifiques sur le trouble psychiatrique, afin de favoriser l'autonomie, l'alliance thérapeutique et la prévention des rechutes.\n\n"
        "Ses 3 dimensions complémentaires sont :\n"
        "1. Dimension pédagogique / informative : transmission de savoirs objectifs sur les mécanismes du trouble, les symptômes et les traitements. Exemple : expliquer la régulation de la dopamine dans la schizophrénie et les effets attendus des antipsychotiques.\n"
        "2. Dimension psychologique / émotionnelle : travail sur l'acceptation du diagnostic, le partage du vécu, la déculpabilisation des familles et la réduction de la stigmatisation. Exemple : déculpabiliser des parents quant à l'origine du trouble de leur enfant.\n"
        "3. Dimension pratique / comportementale : développement de compétences d'adaptation (coping) et de gestion de crise. Exemple : apprendre au patient à identifier ses signes précoces de rechute (ex: insomnie consécutive) pour déclencher une consultation rapide."
    )
}

for q in questions:
    qid = q["id"]
    if qid in model_answers:
        q["model_answer"] = model_answers[qid]

with open(OPEN_QUESTIONS_PATH, "w", encoding="utf-8") as f:
    json.dump(questions, f, ensure_ascii=False, indent=2)

print("Updated open_questions.json with detailed model answers for all 10 questions!")
