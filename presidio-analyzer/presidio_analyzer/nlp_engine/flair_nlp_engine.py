import flair

from flair.data import Sentence
from flair.models import SequenceTagger

from presidio_analyzer import PresidioLogger
from presidio_analyzer.nlp_engine import NlpArtifacts, NlpEngine

logger = PresidioLogger()


class FlairNlpEngine(NlpEngine):
    """FlairNlpEngine is an abstraction layer over the nlp module.
    It provides processing functionality as well as other queries
    on tokens.
    The FlairNlpEngine uses Flair as its NLP module
    """

    engine_name = "flair"
    is_available = bool(flair)

    def __init__(self, models=None):
        if not models:
            models = {"en": "ner"}
        logger.debug(f"Loading flair models: {models.values()}")

        self.nlp = {
            lang_code: SequenceTagger.load(model_name)
            for lang_code, model_name in models.items()
        }

        # for model_name in models.values():
        #     logger.debug(
        #         "Printing flair model and package details:"
        #         "\n\n {}\n\n".format(spacy.info(model_name))
        #     )

    def process_text(self, text, language):
        """Execute the Flair NLP pipeline on the given text
        and language
        """
        sentence = Sentence(text)
        self.nlp[language].predict(sentence)
        return self.doc_to_nlp_artifact(sentence, language)

    def is_stopword(self, word, language):
        """returns true if the given word is a stop word
        (within the given language)
        """
        # return self.nlp[language].vocab[word].is_stop
        pass

    def is_punct(self, word, language):
        """returns true if the given word is a punctuation word
        (within the given language)
        """
        # return self.nlp[language].vocab[word].is_punct
        pass

    def get_nlp(self, language):
        return self.nlp[language]

    def doc_to_nlp_artifact(self, doc, language):
        tokens = [token.text for token in doc]
        lemmas = [label for label in doc.labels]
        tokens_indices = [token.start_pos for token in doc]
        entities = doc.to_dict(tag_type="ner")["entities"]
        return NlpArtifacts(
            entities=entities,
            tokens=tokens,
            tokens_indices=tokens_indices,
            lemmas=lemmas,
            nlp_engine=self,
            language=language,
        )

    def _get_entities(self, doc):
        entities = doc.to_dict(tag_type="ner")["entities"]
        ent_list = []
        if entities:
            for e in entities:
                entity = str(e["labels"][0].value)
                ent_list.append(entity)
        return ent_list