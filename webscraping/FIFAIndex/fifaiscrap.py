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
    
    try: #get basic infomation
        basicInfo = driver.find_element_by_xpath("""/html/body/div[3]/div[2]/div[2]/div[1]""").text.split('\n')
    except:
        print(url + ' basic info not found')
        Height = '?'
        Weight = '?'
        PreferredFoot = '?'
        BirthDate = '?'
        Age = '?'
        PreferredPositions = '?'
        PlayerWorkRate = '?'
        
    name = basicInfo[0]
    country = basicInfo[1]
    overallScore = basicInfo[3].split()[0]
    
    for index1 in range(len(basicInfo)):
        if re.search(r'\bFHeight\b', basicInfo[index1]):
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
    print(basicInfo)
    
    
    try: #get team infomation
        teamInfo = driver.find_element_by_xpath("""/html/body/div[3]/div[2]/div[2]/div[2]""").text.split('\n')
    except:
        print(url + ' team info not found')
    
    for index2 in range(len(basicInfo)):
        Team = teamInfo[5]
        
        if re.search(r'\bPosition\b', basicInfo[index2]):
            teamPosition = teamInfo[index2 + 1] 
        
        if re.search(r'\bJoined Club\b', basicInfo[index2]):
            year = teamInfo[index2 + 1]
        
        if re.search(r'\bContract Length\b', basicInfo[index2]):
            contract = teamInfo[index2 + 1]
    print(teamInfo)

    
    try: #get performance infomation
        performInfo = driver.find_element_by_xpath("""/html/body/div[3]/div[2]/div[2]/div[3]""").text.split('\n')
    except:
        print(url + ' performance info not found') 
    
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
        
        if re.search(r'\bShotPower\b', performInfo[index3]):
            ShotPower = performInfo[index3 + 1]
        
        if re.search(r'\bFinishing\b', performInfo[index3]):
            Finishing = performInfo[index3 + 1]
        
        if re.search(r'\bLong Shots\b', performInfo[index3]):
            LongShots = performInfo[index3 + 1]
        
        if re.search(r'\bCurve\b', performInfo[index3]):
            Curve = performInfo[index3 + 1]
        
        if re.search(r'\bFK Acc.\b', performInfo[index3]):
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
    print(performInfo)

    return 0

singlePlayer('https://www.fifaindex.com/player/20801/cristiano-ronaldo/')
driver.quit()
