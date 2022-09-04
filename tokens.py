CLEAN_TOKEN_STEP1 = '[\=;\\"\<\>,)(]'
CLEAN_TOKEN_STEP2 = "[']"

def initTokensMap():
    tokensList = []
    tokensCombo = []
    tokensList.append(Token('AMAZON_AWS', '([^A-Z0-9]|^)(AKIA)[A-Z0-9]{12,}',['EXAMPLE']))

## Tokens which need two keys to be interesting ##

    twilioSID = Token('TWILIO_SID', '(AC[a-f0-9]{32}[^a-f0-9])', None, 1)
    twilioAUTH = Token('TWILIO_AUTH', '\W[a-f0-9]{32}\W', None, 2)
    tokensCombo.append(TokenCombo('TWILIO', [twilioSID, twilioAUTH]))
 
    return tokensList, tokensCombo

class Token:

    def __init__(self, name, regex, blacklist = [], displayOrder = 1):
        self.name = name
        self.regex = regex
        self.blacklist = blacklist
        self.displayOrder = displayOrder
    
    def getName(self):
        return self.name
    
    def getRegex(self):
        return self.regex

    def getBlacklist(self):
        return self.blacklist

    def getDisplayOrder(self):
        return self.displayOrder

class TokenCombo:

    def __init__(self, name, tokensList = []):
        self.tokensList = tokensList
        self.name = name
    
    def getTokens(self):
        return self.tokensList
    
    def getName(self):
        return self.name


