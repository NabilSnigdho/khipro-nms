"""
https://github.com/OpenBangla/riti/blob/master/src/fixed/chars.rs

The Unicode Standard 8.0
http://www.unicode.org/charts/
http://www.unicode.org/charts/PDF/U0980.pdf

The Bengali script is also known as Bangla. In Assam, the
preferred name of the script is Asamiya or Assamese. The
Assamese language has also been written historically using
distinct regional scripts known as Kamrupi.

We have changed some Character names according to Bangla language or phonetic equivalent.
Actual names are denoted by comments
"""

# Various signs
B_SIGN_ANJI = "\u0980"
B_CHANDRA = "\u0981"
B_ANUSHAR = "\u0982"  # BENGALI SIGN ANUSVARA
B_BISHARGA = "\u0983"  # BENGALI SIGN VISARGA

# Independent vowels
B_A = "\u0985"
B_AA = "\u0986"
B_I = "\u0987"
B_II = "\u0988"
B_U = "\u0989"
B_UU = "\u098A"
B_RRI = "\u098B"  # BENGALI LETTER VOCALIC R
B_VOCALIC_L = "\u098C"
B_E = "\u098F"
B_OI = "\u0990"  # BENGALI LETTER AI
B_O = "\u0993"
B_OU = "\u0994"

# Consonants
B_K = "\u0995"
B_KH = "\u0996"
B_G = "\u0997"
B_GH = "\u0998"
B_NGA = "\u0999"
B_C = "\u099A"
B_CH = "\u099B"
B_J = "\u099C"
B_JH = "\u099D"
B_NYA = "\u099E"
B_TT = "\u099F"
B_TTH = "\u09A0"
B_DD = "\u09A1"
B_DDH = "\u09A2"
B_NN = "\u09A3"
B_T = "\u09A4"
B_TH = "\u09A5"
B_D = "\u09A6"
B_DH = "\u09A7"
B_N = "\u09A8"
B_P = "\u09AA"
B_PH = "\u09AB"
B_B = "\u09AC"
B_BH = "\u09AD"
B_M = "\u09AE"
B_Z = "\u09AF"
B_R = "\u09B0"
B_L = "\u09B2"
B_SH = "\u09B6"
B_SS = "\u09B7"
B_S = "\u09B8"
B_H = "\u09B9"

# Various signs
B_SIGN_NUKTA = "\u09BC"  # for extending the alphabet to new letters
B_SIGN_AVAGRAHA = "\u09BD"

# Dependent vowel signs (kars)
B_AA_KAR = "\u09BE"
B_I_KAR = "\u09BF"
B_II_KAR = "\u09C0"
B_U_KAR = "\u09C1"
B_UU_KAR = "\u09C2"
B_RRI_KAR = "\u09C3"  # BENGALI VOWEL SIGN VOCALIC R
B_VOCALIC_RR = "\u09C4"  # BENGALI VOWEL SIGN VOCALIC RR
B_E_KAR = "\u09C7"
B_OI_KAR = "\u09C8"

# Two-part dependent vowel signs
B_O_KAR = "\u09CB"
B_OU_KAR = "\u09CC"  # BENGALI VOWEL SIGN AU

# Virama or Hasant
B_HASANTA = "\u09CD"

# Additional consonant
B_KHANDATTA = "\u09CE"

# Sign
B_LENGTH_MARK = "\u09D7"  # BENGALI AU LENGTH MARK

# Additional consonants
B_RR = "\u09DC"  # BENGALI LETTER RRA
B_RH = "\u09DD"  # BENGALI LETTER RHA
B_Y = "\u09DF"  # BENGALI LETTER YYA

# Additional vowels for Sanskrit
B_SANSKRIT_RR = "\u09E0"  # BENGALI LETTER VOCALIC RR
B_SANSKRIT_LL = "\u09E1"  # BENGALI LETTER VOCALIC LL
B_SIGN_L = "\u09E2"  # BENGALI VOWEL SIGN VOCALIC L
B_SIGN_LL = "\u09E3"  # BENGALI VOWEL SIGN VOCALIC LL

# Reserved
"""
For viram punctuation, use the generic Indic 0964 and 0965.  *
Note that these punctuation marks are referred to as dahri   *
and double dahri in Bangla.                                  *
"""
B_DARI = "\u0964"
B_DDARI = "\u0965"

# Digits
B_0 = "\u09E6"
B_1 = "\u09E7"
B_2 = "\u09E8"
B_3 = "\u09E9"
B_4 = "\u09EA"
B_5 = "\u09EB"
B_6 = "\u09EC"
B_7 = "\u09ED"
B_8 = "\u09EE"
B_9 = "\u09EF"

# Additions for Assamese
B_RM = "\u09F0"  # BENGALI LETTER RA WITH MIDDLE DIAGONAL
B_RL = "\u09F1"  # BENGALI LETTER RA WITH LOWER DIAGONAL

# Currency signs
B_CRTAKA_M = "\u09F2"  # BENGALI RUPEE MARK = taka
B_CRTAKA = "\u09F3"  # BENGALI RUPEE SIGN = Bangladeshi taka

# Historic symbols for fractional values
B_CURRENCYNUMERATOR_ONE = "\u09F4"
B_CURRENCYNUMERATOR_TWO = "\u09F5"
B_CURRENCYNUMERATOR_THREE = "\u09F6"
B_CURRENCYNUMERATOR_FOUR = "\u09F7"
B_CURRENCYNUMERATOR_LESS = "\u09F8"
B_CURRENCYNUMERATOR_SIXTEEN = "\u09F9"

# Sign
B_SIGN_ISSHAR = "\u09FA"

# Historic currency sign
B_CURRENCYGANDA = "\u09FB"

# Unicode Addition
ZWJ = "\u200D"
ZWNJ = "\u200C"
