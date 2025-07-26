"""Type definitions for Japanese morphological analysis"""

from enum import Enum


class PartOfSpeech(Enum):
    """Part of Speech (品詞)"""

    NOUN = "名詞"
    VERB = "動詞"
    ADJECTIVE = "形容詞"
    ADVERB = "副詞"
    PARTICLE = "助詞"
    AUXILIARY_VERB = "助動詞"
    SYMBOL = "記号"
    PREFIX = "接頭詞"
    SUFFIX = "接尾"
    CONJUNCTION = "接続詞"
    INTERJECTION = "感動詞"
    ADNOMINAL = "連体詞"
    UNKNOWN = "未知語"


class DetailType(Enum):
    """Unified detailed classification"""

    # Noun-related
    NOUN_GENERAL = "一般"
    NOUN_PROPER = "固有名詞"
    NOUN_PERSONAL = "人名"
    NOUN_SURNAME = "姓"
    NOUN_ORGANIZATION = "組織"
    NOUN_NUMERAL = "数"
    NOUN_COUNTER = "助数詞"
    NOUN_ADVERBIAL = "副詞可能"
    NOUN_SAHEN = "サ変接続"
    NOUN_ADJECTIVE_VERBAL = "形容動詞語幹"
    NOUN_SUFFIX = "接尾"
    NOUN_VERBAL = "動詞非自立的"
    NOUN_SPECIAL = "特殊"
    NOUN_NON_INDEPENDENT = "非自立"
    NOUN_PRONOUN = "代名詞"
    NOUN_REGION = "地域"
    NOUN_COUNTRY = "国"
    NOUN_ADVERBIALIZATION = "副詞化"
    NOUN_CONNECTION = "名詞接続"

    # Verb-related
    VERB_INDEPENDENT = "自立"
    VERB_NON_INDEPENDENT = "非自立"
    VERB_SUFFIX = "接尾"

    # Particle-related
    PARTICLE_CASE = "格助詞"
    PARTICLE_CONJUNCTIVE = "接続助詞"
    PARTICLE_ADNOMINAL = "連体化"
    PARTICLE_FINAL = "終助詞"
    PARTICLE_PARALLEL = "並立助詞"
    PARTICLE_BINDING = "係助詞"
    PARTICLE_ADVERBIAL = "副助詞"
    PARTICLE_INTERJECTIONAL = "間投助詞"
    PARTICLE_MULTIPLE = "副助詞／並立助詞／終助詞"

    # Symbol-related
    SYMBOL_PERIOD = "句点"
    SYMBOL_COMMA = "読点"
    SYMBOL_GENERAL = "一般"
    SYMBOL_ALPHABET = "アルファベット"

    # Others
    COMPOUND = "連語"
    QUOTATION = "引用"
    UNKNOWN = "*"


class InflectionForm(Enum):
    """Verb inflection forms"""

    BASIC = "基本形"
    STEM = "語幹"
    INFLECTED = "連用形"
    INFLECTED_TE = "連用タ接続"
    INFLECTED_GO = "連用ゴザイ"
    IMPERATIVE = "命令ｉ"
    IMPERATIVE_E = "命令ｅ"
    IMPERATIVE_YO = "命令ｙｏ"
    IMPERATIVE_RO = "命令ｒｏ"
    CONDITIONAL = "仮定形"
    ATTRIBUTIVE = "連体形"
    UNINFLECTED = "未然形"
    UNINFLECTED_NEGATIVE = "未然ウ接続"
    UNINFLECTED_SPECIAL = "未然特殊"
    NOUN_CONNECTION = "体言接続"
    UNKNOWN = "*"


class InflectionType(Enum):
    """Inflection types (merged from previous inflection and auxiliary verb types)"""

    GODAN = "五段・ラ行"
    GODAN_AL = "五段・ラ行アル"
    GODAN_SPECIAL = "五段・ラ行特殊"
    GODAN_KA_CONTRACTED = "五段・カ行促音便"
    GODAN_KA_IBIN = "五段・カ行イ音便"
    GODAN_WA_CONTRACTED = "五段・ワ行促音便"
    GODAN_MA = "五段・マ行"
    GODAN_GA = "五段・ガ行"
    GODAN_BA = "五段・バ行"
    GODAN_SA = "五段・サ行"
    ICHIDAN = "一段"
    SAHEN = "サ変・スル"
    KA_GODAN = "カ変・クル"
    KA_GODAN_SPECIAL = "カ変・来ル"
    SA_GODAN = "サ変・−ズル"
    SA_GODAN_SPECIAL = "サ変・−ズル"
    ADJECTIVE_ISTEM = "形容詞・イ段"
    ADJECTIVE_AUO = "形容詞・アウオ段"
    UNCHANGING = "不変化型"

    SPECIAL_TA = "特殊・タ"
    SPECIAL_DA = "特殊・ダ"
    SPECIAL_DESU = "特殊・デス"
    SPECIAL_MASU = "特殊・マス"
    SPECIAL_NAI = "特殊・ナイ"
    SPECIAL_TAI = "特殊・タイ"
    SPECIAL_RASHII = "特殊・ラシイ"
    SPECIAL_YOU = "特殊・ヨウ"
    SPECIAL_MI = "特殊・ミ"
    SPECIAL_SERU = "特殊・セル"
    SPECIAL_RERU = "特殊・レル"
    SPECIAL_RU = "特殊・ル"
    SPECIAL_U = "特殊・ウ"
    SPECIAL_YOU_SPECIAL = "特殊・ヨウ・ニ"
    SPECIAL_DA_SPECIAL = "特殊・ダ・ニ"
    SPECIAL_DA_SPECIAL2 = "特殊・ダ・ニ・ダ"
    SPECIAL_DA_SPECIAL3 = "特殊・ダ・ニ・デ"
    SPECIAL_DA_SPECIAL4 = "特殊・ダ・ニ・デ・ダ"
    SPECIAL_DA_SPECIAL5 = "特殊・ダ・ニ・デ・ダ・ニ"
    SPECIAL_DA_SPECIAL6 = "特殊・ダ・ニ・デ・ダ・ニ・ダ"
    SPECIAL_DA_SPECIAL7 = "特殊・ダ・ニ・デ・ダ・ニ・ダ・ニ"
    SPECIAL_DA_SPECIAL8 = "特殊・ダ・ニ・デ・ダ・ニ・ダ・ニ・ダ"
    SPECIAL_DA_SPECIAL9 = "特殊・ダ・ニ・デ・ダ・ニ・ダ・ニ・ダ・ニ"
    SPECIAL_DA_SPECIAL10 = "特殊・ダ・ニ・デ・ダ・ニ・ダ・ニ・ダ・ニ・ダ"
    UNKNOWN = "*"
