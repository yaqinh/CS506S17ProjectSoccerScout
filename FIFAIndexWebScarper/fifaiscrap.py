from pyvirtualdisplay import Display
from selenium import webdriver
import re
import time
import pandas as pd
import numpy as np


display = Display(visible=0, size=(800, 600))
display.start()
driver = webdriver.Chrome() #initialize the webdriver


def singlePlayer(url):
    driver.get(url)
    singleList = []
    
    name = '?'
    country = '?'
    overallScore = '?'
    potentialScore = '?'
    Height = '?'
    Weight = '?'
    PreferredFoot = '?'
    BirthDate = '?'
    Age = '?'
    PreferredPositions = '?'
    PlayerWorkRate = '?'
    team = '?'
    teamPosition = '?'
    year = '?'
    contract = '?'
    BallControl = '?'
    Dribbling = '?'
    Marking = '?'
    SlideTackle = '?'
    StandTackle = '?'
    Aggression = '?'
    Reactions = '?'
    AttPosition = '?'
    Interceptions = '?'
    Vision = '?'
    Composure = '?'
    Crossing = '?'
    ShortPass = '?'
    LongPass = '?'
    Acceleration = '?'
    Stamina = '?'
    Strength = '?'
    Balance = '?'
    SprintSpeed = '?'
    Agilityd = '?'
    Jumping = '?'
    Heading = '?'
    ShotPower = '?'
    Finishing = '?'
    LongShots = '?'
    Curve = '?'
    FKAcc = '?'
    Penalties = '?'
    Volleys = '?'
    GKPositioning = '?'
    GKDiving = '?'
    GKHandling = '?'
    GKKicking = '?'
    GKReflexes = '?'
    
    try: #get basic infomation
        basicInfo = driver.find_element_by_xpath("""/html/body/div[3]/div[2]/div[2]/div[1]""").text.split('\n')
        name = basicInfo[0]
        country = basicInfo[1]
        overallScore = basicInfo[3].split()[0]
        potentialScore = basicInfo[3].split()[1]
        for index1 in range(len(basicInfo)):
            if re.search(r'\bHeight\b', basicInfo[index1]):
                Height = basicInfo[index1 + 1]
        
            if re.search(r'\bWeight\b', basicInfo[index1]):
                Weight = basicInfo[index1 + 1]
        
            if re.search(r'\bPreferred Foot\b', basicInfo[index1]):
                PreferredFoot = basicInfo[index1 + 1]
        
            if re.search(r'\bBirth Date\b', basicInfo[index1]):
                BirthDate = basicInfo[index1 + 1]
        
            if re.search(r'\bAge\b', basicInfo[index1]):
                Age = basicInfo[index1 + 1]
        
            if re.search(r'\bPreferred Positions\b', basicInfo[index1]):
                PreferredPositions = basicInfo[index1 + 1]
        
            if re.search(r'\bPlayer Work Rate\b', basicInfo[index1]):
                PlayerWorkRate = basicInfo[index1 + 1]
    except:
        print(url + ' basic info not found')

    #print(basicInfo)
    singleList.append(name)
    singleList.append(country)
    singleList.append(overallScore)
    singleList.append(potentialScore)
    singleList.append(Height)
    singleList.append(Weight)
    singleList.append(PreferredFoot)
    singleList.append(BirthDate)
    singleList.append(Age)
    singleList.append(PreferredPositions)
    singleList.append(PlayerWorkRate)
    
    
    try: #get team infomation
        teamInfo = driver.find_element_by_xpath("""/html/body/div[3]/div[2]/div[2]/div[2]""").text.split('\n')
        team = teamInfo[5]
        if team == 'Joined Club': #For those player who does not have country team infomation
            team = teamInfo[0]
            
        for index2 in range(len(teamInfo)):
            if re.search(r'\bPosition\b', teamInfo[index2]):
                teamPosition = teamInfo[index2 + 1] 
        
            if re.search(r'\bJoined Club\b', teamInfo[index2]):
                year = teamInfo[index2 + 1]
        
            if re.search(r'\bContract Length\b', teamInfo[index2]):
                contract = teamInfo[index2 + 1]
    except:
        print(url + ' team info not found')
        
    #print(teamInfo)
    singleList.append(team)
    singleList.append(teamPosition)
    singleList.append(year)
    singleList.append(contract)

    
    try: #get performance infomation
        performInfo = driver.find_element_by_xpath("""/html/body/div[3]/div[2]/div[2]/div[3]""").text.split('\n')
        for index3 in range(len(performInfo)):
            if re.search(r'\bBall Control\b', performInfo[index3]):
                BallControl = performInfo[index3 + 1]
        
            if re.search(r'\bDribbling\b', performInfo[index3]):
                Dribbling = performInfo[index3 + 1]
    
            if re.search(r'\bMarking\b', performInfo[index3]):
                Marking = performInfo[index3 + 1]
        
            if re.search(r'\bSlide Tackle\b', performInfo[index3]):
                SlideTackle = performInfo[index3 + 1]
        
            if re.search(r'\bStand Tackle\b', performInfo[index3]):
                StandTackle = performInfo[index3 + 1]
        
            if re.search(r'\bAggression\b', performInfo[index3]):
                Aggression = performInfo[index3 + 1]
        
            if re.search(r'\bReactions\b', performInfo[index3]):
                Reactions = performInfo[index3 + 1]
        
            if re.search(r'\bAtt. Position\b', performInfo[index3]):
                AttPosition = performInfo[index3 + 1]
        
            if re.search(r'\bInterceptions\b', performInfo[index3]):
                Interceptions = performInfo[index3 + 1]
        
            if re.search(r'\bVision\b', performInfo[index3]):
                Vision = performInfo[index3 + 1]
        
            if re.search(r'\bComposure\b', performInfo[index3]):
                Composure = performInfo[index3 + 1]
        
            if re.search(r'\bCrossing\b', performInfo[index3]):
                Crossing = performInfo[index3 + 1]
        
            if re.search(r'\bShort Pass\b', performInfo[index3]):
                ShortPass = performInfo[index3 + 1]
        
            if re.search(r'\bLong Pass\b', performInfo[index3]):
                LongPass = performInfo[index3 + 1]
        
            if re.search(r'\bAcceleration\b', performInfo[index3]):
                Acceleration = performInfo[index3 + 1]
        
            if re.search(r'\bStamina\b', performInfo[index3]):
                Stamina = performInfo[index3 + 1]
        
            if re.search(r'\bStrength\b', performInfo[index3]):
                Strength = performInfo[index3 + 1]
        
            if re.search(r'\bBalance\b', performInfo[index3]):
                Balance = performInfo[index3 + 1]
        
            if re.search(r'\bSprint Speed\b', performInfo[index3]):
                SprintSpeed = performInfo[index3 + 1]
        
            if re.search(r'\bAgility\b', performInfo[index3]):
                Agilityd = performInfo[index3 + 1]
        
            if re.search(r'\bJumping\b', performInfo[index3]):
                Jumping = performInfo[index3 + 1]
        
            if re.search(r'\bHeading\b', performInfo[index3]):
                Heading = performInfo[index3 + 1]
        
            if re.search(r'\bShot Power\b', performInfo[index3]):
                ShotPower = performInfo[index3 + 1]
        
            if re.search(r'\bFinishing\b', performInfo[index3]):
                Finishing = performInfo[index3 + 1]
        
            if re.search(r'\bLong Shots\b', performInfo[index3]):
                LongShots = performInfo[index3 + 1]
        
            if re.search(r'\bCurve\b', performInfo[index3]):
                Curve = performInfo[index3 + 1]
        
            if re.search(r'\bFK Acc\b', performInfo[index3]):
                FKAcc = performInfo[index3 + 1]
        
            if re.search(r'\bPenalties\b', performInfo[index3]):
                Penalties = performInfo[index3 + 1] 
        
            if re.search(r'\bVolleys\b', performInfo[index3]):
                Volleys = performInfo[index3 + 1]
        
            if re.search(r'\bGK Positioning\b', performInfo[index3]):
                GKPositioning = performInfo[index3 + 1]
        
            if re.search(r'\bGK Diving\b', performInfo[index3]):
                GKDiving = performInfo[index3 + 1]
        
            if re.search(r'\bGK Handling\b', performInfo[index3]):
                GKHandling = performInfo[index3 + 1]
        
            if re.search(r'\bGK Kicking\b', performInfo[index3]):
                GKKicking = performInfo[index3 + 1]
        
            if re.search(r'\bGK Reflexes\b', performInfo[index3]):
                GKReflexes = performInfo[index3 + 1]
    except:
        print(url + ' performance info not found') 
    
    singleList.append(BallControl)
    singleList.append(Dribbling)
    singleList.append(Marking)
    singleList.append(SlideTackle)
    singleList.append(StandTackle)
    singleList.append(Aggression)
    singleList.append(Reactions)
    singleList.append(AttPosition)
    singleList.append(Interceptions)
    singleList.append(Vision)
    singleList.append(Composure)
    singleList.append(Crossing)
    singleList.append(ShortPass)
    singleList.append(LongPass)
    singleList.append(Acceleration)
    singleList.append(Stamina)
    singleList.append(Strength)
    singleList.append(Balance)
    singleList.append(SprintSpeed)
    singleList.append(Agilityd)
    singleList.append(Jumping)
    singleList.append(Heading)
    singleList.append(ShotPower)
    singleList.append(Finishing)
    singleList.append(LongShots)
    singleList.append(Curve)
    singleList.append(FKAcc)
    singleList.append(Penalties)
    singleList.append(Volleys)
    singleList.append(GKPositioning)
    singleList.append(GKDiving)
    singleList.append(GKHandling)
    singleList.append(GKKicking)
    singleList.append(GKReflexes)
    #print(performInfo)
    
    return singleList


def findAllLeagueUrl(firstUrl):
    URL = firstUrl
    playerListUrl = [firstUrl]

    while (1):
        driver.get(URL)
        try:
            #find the url for following player list in the Next Page button 
            URL = driver.find_element_by_xpath("""/html/body/div[3]/div[2]/div[2]/div[3]/ul/li[2]/a""").get_attribute("href")
            playerListUrl.append(URL)
        except:
            #print("End of player list url")
            break
    
    return playerListUrl


def findAllPlayerUrl(leagueUrl):
    time.sleep(np.random.randint(2,  high=5))    
    driver.get(leagueUrl)
    playerList = []
    try:
        elems = driver.find_elements_by_xpath("//a[@href]")
        for elem in elems:
            url = elem.get_attribute("href")
            if re.search(r'\bhttps://www.fifaindex.com/player/\b' ,url):
                playerList.append(url)
    except:
        print(leagueUrl + ' urls not found')
    
    return set(playerList)


def main():
    header = ['Name', 'Country', 'OverallScore', 'PotentialScore', 'Height', 'Weight', 'PreferredFoot', 'BirthDate', 
          'Age', 'PreferredPositions', 'PlayerWorkRate', 'Team', 'TeamPosition', 'Year', 'Contract', 'BallControl',
          'Dribbling', 'Marking', 'SlideTackle', 'StandTackle', 'Aggression', 'Reactions', 'AttPosition', 'Interceptions',
          'Vision', 'Composure', 'Crossing', 'ShortPass', 'LongPass', 'Acceleration', 'Stamina', 'Strength', 'Balance',
          'SprintSpeed', 'Agility', 'Jumping', 'Heading', 'ShotPower', 'Finishing', 'LongShots', 'Curve', 'FKAcc', 
          'Penalties', 'Volleys', 'GKPositioning', 'GKDiving', 'GKHandling', 'GKKicking', 'GKReflexes']

    leagueListUrl = findAllLeagueUrl(firstUrl)
    leagueList = []
    for leagueUrl in leagueListUrl:
        playerset = findAllPlayerUrl(leagueUrl)
        print('current league url being scraped' + leagueUrl)
        for playerUrl in playerset:
            leagueList.append(playerUrl) #get all the url for every player in the league
    
    playerList = []
    for playerUrl in leagueList:
        singleList = singlePlayer(playerUrl) #get the detailed data for every player
        playerList.append(singleList)
    
    players = pd.DataFrame(playerList, columns=header)
    
    print('CSV write started')
    players.to_csv('FIFIndex_BPL_April_6_players.csv', index=True, header=header, mode='w') #dump to csv
    print('Success')
    
    return 0
    

if __name__ == '__main__':
    main('https://www.fifaindex.com/players/fifa17_126/?league=13') #The first page url of FIFA player list in a league
    
