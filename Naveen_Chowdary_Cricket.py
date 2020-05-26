import random

Mumbai_Indians_Squad = []

Team_II_Squad = []


# ==========================================================================================================

class Cricketer:
    def __init__(self, Mumbai_Indians_Squad):

        self.Runs = random.randint(20, 80)

        self.Balls = random.randint(10, 40)

        self.Total_Balls = 0

        self.Total_Runs = 0

        self.Total_Runs_Team_II = 0

        self.Total_Runs_Mumbai = 0

        self.Total_Sixes = 0

        self.Sixes = self.Runs // 12

        self.Strike_Rate = round((self.Runs / self.Balls) * 100, 2)

    def Series(self):

        for i in range(5):
            self.Total_Balls = 0

            self.Total_Runs = 0

            self.Total_Sixes = 0

            count = 0

            # def Batting_Mumbai(self):

            print("{}   MATCH NO -- {}   {}".format(60 * "#", i + 1, 60 * "#"), end="\n\n\n")

            print("--------------------::  Innings I  ::------------------", end="\n\n")

            print(
                "{:<5}{:<25} {:<9} {:<43} {:<19} {:<10} {:<10} {:<10} Strike Rate".format(" ", "Batsman", " ", " ", " ",
                                                                                          "Runs", "Balls", "Sixes"),
                end="\n\n\n")

            for squad in range(0, 11):

                self.Innings_Played = 0

                self.Runs = random.randint(0, 130)

                self.Sixes = self.Runs // 20

                if self.Runs <= 130 and self.Runs > 100:
                    self.Balls = random.randint(80, 100)
                elif self.Runs > 60 and self.Runs <= 100:
                    self.Balls = random.randint(50, 60)
                else:
                    self.Balls = random.randint(20, 40)

                self.Strike_Rate = round((self.Runs / self.Balls) * 100, 2)

                # ================================================

                Bowled_By_List_Team_II = []

                for bowl in range(5, 11):
                    Bowled_By_List_Team_II.append(Team_II_Squad[bowl])

                wicket_type = ["Caught ", "Hit Wicket", "Bowled", "Stumped", "Caught And Bowled"]

                caught_by = random.choice(Team_II_Squad)

                wicket_type_given = random.choice(wicket_type)

                is_wk = "(Wk)"

                for players in range(0, 11):
                    if is_wk in Team_II_Squad[players]:
                        Wicky = Team_II_Squad[players]

                if wicket_type_given == "Stumped":
                    type = wicket_type_given + " By " + Wicky

                elif wicket_type_given == "Bowled" or wicket_type_given == "Hit Wicket" or wicket_type_given == "Caught And Bowled":

                    Bowled_by = random.choice(Bowled_By_List_Team_II)

                    type = wicket_type_given + " By " + Bowled_by


                else:

                    type = wicket_type_given + " By " + caught_by

                if self.Total_Balls <= 300:
                    print("{:<5}{:<25} {:<9} {:<43} {:<20} {:<10} {:<10} {:<10} {}".format(" ",
                                                                                           Mumbai_Indians_Squad[squad],
                                                                                           " ", type, " ", self.Runs,
                                                                                           self.Balls, self.Sixes,
                                                                                           self.Strike_Rate),
                          end="\n\n")
                    self.Total_Runs += self.Runs
                    self.Total_Balls += self.Balls
                    self.Total_Sixes += self.Sixes
                    count = count + 1
                    self.Innings_Played += 1

                    """

                    Match_Dictionary_Mumbai_Batting = {'Batsman': Mumbai_Indians_Squad[squad], 'Wicket Type': type,
                                                       'Runs': self.Runs,
                                                       'Balls': self.Balls, 'Sixes': self.Sixes,
                                                       'Strike Rate': self.Strike_Rate}

                    #print(Match_Dictionary_Mumbai_Batting)
                    """

                    for key in Stats_Of_Mumbai:

                        if key == Mumbai_Indians_Squad[squad]:
                            # print(key)

                            Stats_Of_Mumbai[key]['Innings_Played'] += self.Innings_Played
                            Stats_Of_Mumbai[key]['Runs'] += self.Runs
                            Stats_Of_Mumbai[key]['Balls'] += self.Balls
                            Stats_Of_Mumbai[key]['Sixes'] += self.Sixes



                else:
                    print("{:<5}{:<25} ".format(" ", Mumbai_Indians_Squad[squad]), end="\n\n")

            print("", end="\n")
            print("{:<5}{:<25} {:<9} {:<43} {:<20} {:<10} {:<10} {:<10} ".format(" ", "Total", " ", " ", " ",
                                                                                 self.Total_Runs, "50.0",
                                                                                 self.Total_Sixes), end="\n\n\n")

            self.Total_Runs_Mumbai = self.Total_Runs

            # ===================================================================================================================

            print("{:<5}{:<25} {:<30} {:<10} {:<10} {:<10} Economy".format(" ", "Bowler", " ", "Overs", "Runs",
                                                                           "Wickets"),
                  end="\n\n\n")

            i = 0
            self.Bowler_1 = 0
            self.Bowler_2 = 0
            self.Bowler_3 = 0
            self.Bowler_4 = 0
            self.Bowler_5 = 0
            self.Bowler_6 = 0

            self.Bowler_1_Overs = 0
            self.Bowler_2_Overs = 0
            self.Bowler_3_Overs = 0
            self.Bowler_4_Overs = 0
            self.Bowler_5_Overs = 0
            self.Bowler_6_Overs = 0

            self.Bowler_1_wick = 0
            self.Bowler_2_wick = 0
            self.Bowler_3_wick = 0
            self.Bowler_4_wick = 0
            self.Bowler_5_wick = 0
            self.Bowler_6_wick = 0

            Var = True

            while Var:
                if self.Bowler_1 + self.Bowler_2 + self.Bowler_3 + self.Bowler_4 + self.Bowler_5 + self.Bowler_6 == self.Total_Runs_Mumbai and self.Bowler_1_wick + self.Bowler_2_wick + self.Bowler_3_wick + self.Bowler_4_wick + self.Bowler_5_wick + self.Bowler_6_wick == count and self.Bowler_1_Overs + self.Bowler_2_Overs + self.Bowler_3_Overs + self.Bowler_4_Overs + self.Bowler_5_Overs + self.Bowler_6_Overs == 50:
                    Var = False

                else:
                    self.Bowler_1 = random.randint(20, 90)
                    self.Bowler_2 = random.randint(20, 90)
                    self.Bowler_3 = random.randint(20, 90)
                    self.Bowler_4 = random.randint(20, 90)
                    self.Bowler_5 = random.randint(20, 90)
                    self.Bowler_6 = random.randint(20, 90)

                    self.Bowler_1_Overs = random.randint(8, 10)
                    self.Bowler_2_Overs = random.randint(8, 10)
                    self.Bowler_3_Overs = random.randint(8, 10)
                    self.Bowler_4_Overs = random.randint(8, 10)
                    self.Bowler_5_Overs = random.randint(8, 10)
                    self.Bowler_6_Overs = random.randint(8, 10)

                    self.Bowler_1_wick = random.randint(0, 3)
                    self.Bowler_2_wick = random.randint(0, 3)
                    self.Bowler_3_wick = random.randint(0, 3)
                    self.Bowler_4_wick = random.randint(0, 3)
                    self.Bowler_5_wick = random.randint(0, 3)
                    self.Bowler_6_wick = random.randint(0, 3)

            List = [self.Bowler_1, self.Bowler_2, self.Bowler_3, self.Bowler_4, self.Bowler_5, self.Bowler_6]

            List_wick = [self.Bowler_1_wick, self.Bowler_2_wick, self.Bowler_3_wick, self.Bowler_4_wick,
                         self.Bowler_5_wick, self.Bowler_6_wick]

            List_Overs = [self.Bowler_1_Overs, self.Bowler_2_Overs, self.Bowler_3_Overs, self.Bowler_4_Overs,
                          self.Bowler_5_Overs, self.Bowler_6_Overs]
            # print(List)

            for squad in range(5, 11):
                # self.Runs_given = random.randint(24, 52)

                self.Wickets = random.randint(0, 3)

                self.Economy = round(List[i] / List_Overs[i], 1)

                print("{:<5}{:<25} {:<30} {:<10} {:<10} {:<10} {}".format(" ", Team_II_Squad[squad], " ", List_Overs[i],
                                                                          List[i], List_wick[i], self.Economy),
                      end="\n\n")

                Match_Dictionary_Team_II_Bowling = {'Bowler': Team_II_Squad[squad], 'Overs': List_Overs[i],
                                                    'Runs_Given': List[i], 'Wickets Taken': List_wick[i],
                                                    'Economy': self.Economy}

                # print(Match_Dictionary_Team_II_Bowling)
                i = i + 1

            # def Batting_Team_II(self):

            print("", end="\n\n\n")

            print("------------------:: Innigs II :: ------------", end="\n\n")

            print(
                "{:<5}{:<25} {:<9} {:<43}{:<19} {:<10} {:<10} {:<10} Strike Rate".format(" ", "Batsman", " ", " ", " ",
                                                                                         "Runs", "Balls", "Sixes"),
                end="\n\n\n")

            self.Total_Balls = 0
            self.Total_Runs = 0
            self.Total_Sixes = 0

            count = 0

            for squad in range(0, 11):

                self.Innings_Played = 0

                self.Runs = random.randint(0, 130)

                self.Sixes = self.Runs // 20

                if self.Runs <= 130 and self.Runs > 100:
                    self.Balls = random.randint(80, 100)

                elif self.Runs > 60 and self.Runs <= 100:
                    self.Balls = random.randint(50, 60)
                else:
                    self.Balls = random.randint(20, 40)

                self.Strike_Rate = round((self.Runs / self.Balls) * 100, 2)

                # ==================================================================

                Bowled_By_List_Mumbai = []

                for bowl in range(5, 11):
                    Bowled_By_List_Mumbai.append(Mumbai_Indians_Squad[bowl])

                wicket_type = ["Caught ", "Hit Wicket", "Bowled", "Stumped", "Caught And Bowled"]

                caught_by = random.choice(Mumbai_Indians_Squad)

                Bowled_by = random.choice(Bowled_By_List_Mumbai)

                wicket_type_given = random.choice(wicket_type)

                wicket_type_given = random.choice(wicket_type)

                is_wk = "(Wk)"

                for players in range(0, 11):
                    if is_wk in Mumbai_Indians_Squad[players]:
                        Wicky = Mumbai_Indians_Squad[players]

                if wicket_type_given == "Stumped":
                    type = wicket_type_given + " By " + Wicky

                elif wicket_type_given == "Bowled" or wicket_type_given == "Hit Wicket" or wicket_type_given == "Caught And Bowled":
                    type = wicket_type_given + " By " + Bowled_by

                else:

                    type = wicket_type_given + " By " + caught_by

                if self.Total_Balls <= 300:
                    print(
                        "{:<5}{:<25} {:<9} {:<43} {:<20} {:<10} {:<10} {:<10} {}".format(" ", Team_II_Squad[squad], " ",
                                                                                         type, " ", self.Runs,
                                                                                         self.Balls, self.Sixes,
                                                                                         self.Strike_Rate), end="\n\n")
                    self.Total_Runs += self.Runs
                    self.Total_Balls += self.Balls
                    self.Total_Sixes += self.Sixes

                    self.Innings_Played += 1

                    count = count + 1

                    """

                    Match_Dictionary_Team_II_Batting = {'Batsman': Team_II_Squad[squad], 'Wicket Type': type,
                                                        'Runs': self.Runs,
                                                        'Balls': self.Balls, 'Sixes': self.Sixes,
                                                        'Strike Rate': self.Strike_Rate}

                    #print(Match_Dictionary_Team_II_Batting)

                    """

                    for key in Stats_Of_Team_II:

                        if key == Team_II_Squad[squad]:
                            # print(key)

                            Stats_Of_Team_II[key]['Innings_Played'] += self.Innings_Played

                            Stats_Of_Team_II[key]['Runs'] += self.Runs
                            Stats_Of_Team_II[key]['Balls'] += self.Balls
                            Stats_Of_Team_II[key]['Sixes'] += self.Sixes



                else:

                    print("{:<5}{:<25}".format(" ", Team_II_Squad[squad]), end="\n\n")

            print("", end="\n")
            print("{:<5}{:<25} {:<9} {:<43} {:<20} {:<10} {:<10} {:<10} ".format(" ", "Total", " ", " ", " ",
                                                                                 self.Total_Runs, "50.0",
                                                                                 self.Total_Sixes), end="\n\n\n")

            self.Total_Runs_Team_II = self.Total_Runs

            # =====================================================================================

            print("{:<5}{:<25} {:<29} {:<10} {:<10} {:<10} Economy".format(" ", "Bowler", " ", "Overs", "Runs",
                                                                           "Wickets"),
                  end="\n\n\n")

            i = 0
            self.Bowler_1 = 0
            self.Bowler_2 = 0
            self.Bowler_3 = 0
            self.Bowler_4 = 0
            self.Bowler_5 = 0
            self.Bowler_6 = 0

            self.Bowler_1_Overs = 0
            self.Bowler_2_Overs = 0
            self.Bowler_3_Overs = 0
            self.Bowler_4_Overs = 0
            self.Bowler_5_Overs = 0
            self.Bowler_6_Overs = 0

            self.Bowler_1_wick = 0
            self.Bowler_2_wick = 0
            self.Bowler_3_wick = 0
            self.Bowler_4_wick = 0
            self.Bowler_5_wick = 0
            self.Bowler_6_wick = 0

            var = True

            while var:
                if self.Bowler_1 + self.Bowler_2 + self.Bowler_3 + self.Bowler_4 + self.Bowler_5 + self.Bowler_6 == self.Total_Runs_Team_II and self.Bowler_1_wick + self.Bowler_2_wick + self.Bowler_3_wick + self.Bowler_4_wick + self.Bowler_5_wick + self.Bowler_6_wick == count and self.Bowler_1_Overs + self.Bowler_2_Overs + self.Bowler_3_Overs + self.Bowler_4_Overs + self.Bowler_5_Overs + self.Bowler_6_Overs == 50:
                    var = False

                else:
                    self.Bowler_1 = random.randint(20, 90)
                    self.Bowler_2 = random.randint(20, 90)
                    self.Bowler_3 = random.randint(20, 90)
                    self.Bowler_4 = random.randint(20, 90)
                    self.Bowler_5 = random.randint(20, 90)
                    self.Bowler_6 = random.randint(20, 90)

                    self.Bowler_1_Overs = random.randint(7, 10)
                    self.Bowler_2_Overs = random.randint(7, 10)
                    self.Bowler_3_Overs = random.randint(7, 10)
                    self.Bowler_4_Overs = random.randint(7, 10)
                    self.Bowler_5_Overs = random.randint(7, 10)
                    self.Bowler_6_Overs = random.randint(7, 10)

                    self.Bowler_1_wick = random.randint(0, 2)
                    self.Bowler_2_wick = random.randint(0, 2)
                    self.Bowler_3_wick = random.randint(0, 2)
                    self.Bowler_4_wick = random.randint(0, 2)
                    self.Bowler_5_wick = random.randint(0, 2)
                    self.Bowler_6_wick = random.randint(0, 2)

            List = [self.Bowler_1, self.Bowler_2, self.Bowler_3, self.Bowler_4, self.Bowler_5, self.Bowler_6]

            List_wick = [self.Bowler_1_wick, self.Bowler_2_wick, self.Bowler_3_wick, self.Bowler_4_wick,
                         self.Bowler_5_wick, self.Bowler_6_wick]

            List_Overs = [self.Bowler_1_Overs, self.Bowler_2_Overs, self.Bowler_3_Overs, self.Bowler_4_Overs,
                          self.Bowler_5_Overs
                , self.Bowler_6_Overs]
            # print(List)

            for squad in range(5, 11):
                # self.Runs_given = random.randint(24, 52)

                self.Wickets = random.randint(0, 3)

                self.Economy = round(List[i] / List_Overs[i], 1)

                print("{:<5}{:<25} {:<30} {:<10} {:<10} {:<10} {}".format(" ", Mumbai_Indians_Squad[squad], " ",
                                                                          List_Overs[i],
                                                                          List[i], List_wick[i], self.Economy),
                      end="\n\n")

                Match_Dictionary_Mumbai_Bowling = {'Bowler': Mumbai_Indians_Squad[squad], 'Overs': List_Overs[i],
                                                   'Runs_Given': List[i], 'Wickets Taken': List_wick[i],
                                                   'Economy': self.Economy}

                # print(Match_Dictionary_Mumbai_Bowling)
                i = i + 1

            if self.Total_Runs_Mumbai > self.Total_Runs_Team_II:

                self.Result_Runs = self.Total_Runs_Mumbai - self.Total_Runs_Team_II

                print("", end="\n\n")

                print("{:<40}{} Won By {} ".format(" ", Teams[0], self.Result_Runs), end="\n\n\n")
                print(58 * "===", end="\n\n\n")


            elif self.Total_Runs_Mumbai < self.Total_Runs_Team_II:

                self.Result_Runs = self.Total_Runs_Team_II - self.Total_Runs_Mumbai

                print("", end="\n\n")

                print("{:<40} {} Won By {}".format(" ", Teams[1], self.Total_Runs_Team_II - self.Total_Runs_Mumbai),
                      end="\n\n\n")
                print(58 * "===", end="\n\n\n")

    # List_Of_Dictionaries = []

    # Match_Dictionary = {'Batsman':Mumbai_Indians_Squad}


"""
            else:
                print("", end="\n\n")
                print("Wwwwwwoooooooowwwwww  Are You Kidding Me Avengers..... You Gotta be Assemble  Nowww.... It Its Tie  Can you Believe It.. ....... ",end="\n\n")
                print(" We Are Going To Witness A Super Over Tonigt   ... Here We Go ...")
                Super_Over = random.choice[Teams]
                Super_Over_Runs = random.randint(1 , 10)
                print("{} {} Won By {} Runs In The Mighty Super Over...".format(45 * " " , Super_Over , Super_Over_Runs) , end = "\n\n")
                print(58 * "===", end="\n\n\n")


"""

# ======================================================================================================================================

if __name__ == "__main__":
    import json

    Teams = input().split(",")

    Mumbai_Team = json.loads(input())

    Team_II = json.loads(input())

Coin_Spin = ['Bat', 'Bowl']
Toss = random.choice(Coin_Spin)

# ========================================================================================================================================================


print(" ", end="\n\n\n")

Toss_won = random.choice(Teams)
print(
    "Hello... We Bleed Blue.. Welcome To The Wankade .. Its Time For The Toss.. Ganguly Will Spin Coin.. Rohith Calls Annnddddd... ",
    end="\n\n")
print("{}Won The Toss And Choice To {} First".format(Toss_won, Toss))

for keys in Mumbai_Team:
    Mumbai_Indians_Squad.append(Mumbai_Team[keys])

for keys in Team_II:
    Team_II_Squad.append(Team_II[keys])

playing_XI = len(Mumbai_Indians_Squad)

# ==============================================================

# Stats_Of_Mumbai = {}
# Stats_Of_Team_II = {}


Stats_Of_Mumbai = {player: {'Innings_Played': 0, 'Runs': 0, 'Balls': 0, 'Sixes': 0} for player in Mumbai_Indians_Squad}
# print(Stats_Of_Mumbai)

Stats_Of_Team_II = {player: {'Innings_Played': 0, 'Runs': 0, 'Balls': 0, 'Sixes': 0} for player in Team_II_Squad}
# print(Stats_Of_Team_II)


# =============================================================================================================================================


print(" ", end="\n\n\n")

print(
    "{:>10} {} Playing XI are :".format(" ", Teams[0]) + "{:>68}".format(" ") + "{} Playing XI are :".format(Teams[1]))

print("{:>10}=============================".format(" ") + "{:>72}".format(" ") + "================================",
      end="\n\n")

for player in range(playing_XI):
    print("{:>11}{}. {:<30} {:<66}".format(" ", str(player + 1), str(Mumbai_Indians_Squad[player]), " "),
          "{}. {:<30}".format(str(player + 1), str(Team_II_Squad[player])), end="\n\n")

print(" ", end="\n\n\n")

# ===============================================================================================================================


Team_Mumbai = Cricketer(Mumbai_Indians_Squad)
Team_Chennai = Cricketer(Team_II_Squad)

Team_Mumbai.Series()

# print(Stats_Of_Mumbai)
# print(Stats_Of_Team_II)

"""
for key, value in Stats_Of_Mumbai.items():
    print("{:<25} {:<10} {}".format(key, " ", value), end="\n\n")

for key, value in Stats_Of_Team_II.items():
    print("{:<25} {:<10} {}".format(key, " ", value), end="\n\n")

"""
print(
    "{:<25} {:<9} {:<15} {:<9} {:<9} {:<9} {:<9} {:<9}".format(" Batsman ", " ", " Innings ", " Runs", "Balls", "Sixes", "Strike Rate" , "Average"),
    end="\n\n")
for key, value in Stats_Of_Mumbai.items():
    if value['Balls'] !=0:
        print("{:<25} {:<10} {:<15} {:<9} {:<9} {:<9} {:<9} ".format(key, " ", value['Innings_Played'], value['Runs'],
                                                         value['Balls'], value['Sixes'], round((value['Runs']/value['Balls'])*100 , 2))  , end="\n\n")

    else:
        print("{:<25} {:<10} {:<15} {:<9} {:<9} {:<10} {:<10}".format(key, " ", value['Innings_Played'], value['Runs'],
                                                                    value['Balls'], value['Sixes'],
                                                                    '0'),end="\n\n")


print("", end="\n\n\n")
print("{:<25} {:<9} {:<15} {:<9} {:<9} {:<9} {:<9}".format(" Batsman ", " ", " Innings ", " Runs", "Balls", "Sixes", "Strike Rate"),
      end="\n\n")



for key, value in Stats_Of_Team_II.items():
    # print( "{:<25} {:<10} {}".format( key ," " ,  value) , end = "\n\n" )
    if value['Balls'] !=0:
        print("{:<25} {:<10} {:<15} {:<9} {:<9} {:<9} {:<9}".format(key, " ", value['Innings_Played'], value['Runs'],
                                                             value['Balls'], value['Sixes'], round((value['Runs']/value['Balls'])*100 , 2)), end="\n\n")

    else:
        print("{:<25} {:<10} {:<15} {:<9} {:<9} {:<10} {:<10}".format(key, " ", value['Innings_Played'], value['Runs'],
                                                                      value['Balls'], value['Sixes'],
                                                                      '0'), end="\n\n")

"""

Mumbai Indians , Chennai Kings
{"1":"Rohith Sharma (Cap)" , "2":"Quinton DeKock (Wk)" , "3":"Chris Lynn" , "4":"Yuvaraj Singh" , "5":"Kerion Pollard" , "6":"Hardik Pandya" , "7":"Krunal Pandya" , "8":"Lasith Malinga" , "9":"Nathan Coulter-Nile" , "10":"Dhawal Kulakarni" , "11":"Jasprith Bumrah"}
{"1":"Shane Watson" , "2":"Ambati Rayudu" , "3":"Sursh Raina" , "4":"Faf Duplesis" , "5":"M S Dhoni (Cap)&(Wk)" , "6":"Dwayne Bravo" , "7":"Ravindra Jadeja" , "8":"Harbajan Singh" , "9":"Deepak Chahar" , "10":"Shardaul Thakur" , "11":"Josh Hazlewood"}

Mumbai Indians , Royal Challengers
{"1":"Rohith Sharma (Cap)" , "2":"Quinton DeKock (Wk)" , "3":"Chris Lynn" , "4":"Yuvaraj Singh" , "5":"Kerion Pollard" , "6":"Hardik Pandya" , "7":"Krunal Pandya" , "8":"Lasith Malinga" , "9":"Nathan Coulter-Nile" , "10":"Dhawal Kulakarni" , "11":"Jasprith Bumrah"}
{"1":"Aron Finch" , "2":"Ben Stokes" , "3":"Virat Kohli (Cap)" , "4":"A B Devilliers" , "5":"Parthiv Patel (Wk)" , "6":"Devdutt Padikkal" , "7":"Chris Morris" , "8":"Washington Sundar" , "9":"Umesh Yadav" , "10":"Yuzvendra Chahal" , "11":"Dale Steyn"}

India  , Australia
{"1":"Rohith Sharma " , "2":"Shikar Dhawan" , "3":"Virat Kohli " , "4":"Yuvaraj Singh" , "5":"M S Dhoni (Cap)&(Wk)" , "6":"Hardik Pandya" , "7":"Krunal Pandya" , "8":"Ravindra Jadeja" , "9":"Mohammad Shami" , "10":"Deepak Chahar" , "11":"Jasprith Bumrah"}
{"1":"Aron Finch (Cap)" , "2":"David warner" , "3":"Steve Smith (Cap)" , "4":"Glenn Maxwell" , "5":"Marcus Stoinis" , "6":"Aston Turner" , "7":"Nathan Coulter-Nile" , "8":"Mitchell Starc" , "9":"Adam Zampa" , "10":"Pat Cummins" , "11":"Jason Behrendorff"}

Golden Green , Billion Dollers Blue  
{"1":"Naveen Raja " , "2":"Eeshwar Jhon" , "3":"Shourya Varma (Wk)" , "4":"Naresh Anthe" , "5":"Harish " , "6":"Prashanth" , "7":"Pruthvi" , "8":"Manoj" , "9":"Eid Mubharak (Cap)" , "10":"Gagan" , "11":"Dhinakar"}
{"1":"Yenugula Harish " , "2":"Jaya Prakash" , "3":"Rambabu Rambo (Wk)" , "4":"Rakesh Hulk" , "5":"Raghava PET" , "6":"Wakanda Forevar" , "7":"Naveen Chowdary (Cap)" , "8":"Hari Krishna" , "9":"Veera Raghava" , "10":"Mohan Potta" , "11":"Mr Steve Captain"}

Billion Dollers Blue , Royal Challengers
{"1":"Yenugula Harish " , "2":"Jaya Prakash" , "3":"Rambabu Rambo (Wk)" , "4":"Rakesh Hulk" , "5":"Raghava PET" , "6":"Wakanda Forevar" , "7":"Naveen Chowdary (Cap)" , "8":"Hari Krishna" , "9":"Veera Raghava" , "10":"Mohan Potta" , "11":"Mr Steve Captain"}
{"1":"Aron Finch" , "2":"Ben Stokes" , "3":"Virat Kohli (Cap)" , "4":"A B Devilliers" , "5":"Parthiv Patel (Wk)" , "6":"Devdutt Padikkal" , "7":"Chris Morris" , "8":"Washington Sundar" , "9":"Umesh Yadav" , "10":"Yuzvendra Chahal" , "11":"Dale Steyn"}

"""






"""
Out Put  of code
=================




"C:\Naveen Chowdary\Naveen_Pycharm\venv\Scripts\python.exe" "C:/Naveen Chowdary/Naveen_Pycharm/Naveen_cric_3.py"
Golden Green , Billion Dollers Blue  
{"1":"Naveen Raja " , "2":"Eeshwar Jhon" , "3":"Shourya Varma (Wk)" , "4":"Naresh Anthe" , "5":"Harish " , "6":"Prashanth" , "7":"Pruthvi" , "8":"Manoj" , "9":"Eid Mubharak (Cap)" , "10":"Gagan" , "11":"Dhinakar"}
{"1":"Yenugula Harish " , "2":"Jaya Prakash" , "3":"Rambabu Rambo (Wk)" , "4":"Rakesh Hulk" , "5":"Raghava PET" , "6":"Wakanda Forevar" , "7":"Naveen Chowdary (Cap)" , "8":"Hari Krishna" , "9":"Veera Raghava" , "10":"Mohan Potta" , "11":"Mr Steve Captain"}
 


Hello... We Bleed Blue.. Welcome To The Wankade .. Its Time For The Toss.. Ganguly Will Spin Coin.. Rohith Calls Annnddddd... 

Golden Green Won The Toss And Choice To Bowl First
 


           Golden Green  Playing XI are :                                                                     Billion Dollers Blue   Playing XI are :
          =============================                                                                        ================================

           1. Naveen Raja                                                                                       1. Yenugula Harish               

           2. Eeshwar Jhon                                                                                      2. Jaya Prakash                  

           3. Shourya Varma (Wk)                                                                                3. Rambabu Rambo (Wk)            

           4. Naresh Anthe                                                                                      4. Rakesh Hulk                   

           5. Harish                                                                                            5. Raghava PET                   

           6. Prashanth                                                                                         6. Wakanda Forevar               

           7. Pruthvi                                                                                           7. Naveen Chowdary (Cap)         

           8. Manoj                                                                                             8. Hari Krishna                  

           9. Eid Mubharak (Cap)                                                                                9. Veera Raghava                 

           10. Gagan                                                                                             10. Mohan Potta                   

           11. Dhinakar                                                                                          11. Mr Steve Captain              

 


############################################################   MATCH NO -- 1   ############################################################


--------------------::  Innings I  ::------------------

     Batsman                                                                                             Runs       Balls      Sixes      Strike Rate


     Naveen Raja                         Caught And Bowled By Mohan Potta                                 39         33         1          118.18

     Eeshwar Jhon                        Stumped By Rambabu Rambo (Wk)                                    56         20         2          280.0

     Shourya Varma (Wk)                  Stumped By Rambabu Rambo (Wk)                                    97         56         4          173.21

     Naresh Anthe                        Stumped By Rambabu Rambo (Wk)                                    53         34         2          155.88

     Harish                              Caught And Bowled By Mr Steve Captain                            29         27         1          107.41

     Prashanth                           Bowled By Mohan Potta                                            17         24         0          70.83

     Pruthvi                             Hit Wicket By Hari Krishna                                       4          25         0          16.0

     Manoj                               Caught And Bowled By Mohan Potta                                 18         31         0          58.06

     Eid Mubharak (Cap)                  Hit Wicket By Mohan Potta                                        120        87         6          137.93

     Gagan                     

     Dhinakar                  


     Total                                                                                                433        50.0       16         


     Bowler                                                   Overs      Runs       Wickets    Economy


     Wakanda Forevar                                          8          89         0          11.1

     Naveen Chowdary (Cap)                                    9          60         2          6.7

     Hari Krishna                                             8          63         0          7.9

     Veera Raghava                                            8          65         3          8.1

     Mohan Potta                                              9          77         1          8.6

     Mr Steve Captain                                         8          79         3          9.9




------------------:: Innigs II :: ------------

     Batsman                                                                                            Runs       Balls      Sixes      Strike Rate


     Yenugula Harish                     Hit Wicket By Manoj                                              104        91         5          114.29

     Jaya Prakash                        Hit Wicket By Pruthvi                                            74         54         3          137.04

     Rambabu Rambo (Wk)                  Caught And Bowled By Dhinakar                                    102        86         5          118.6

     Rakesh Hulk                         Bowled By Gagan                                                  110        88         5          125.0

     Raghava PET              

     Wakanda Forevar          

     Naveen Chowdary (Cap)    

     Hari Krishna             

     Veera Raghava            

     Mohan Potta              

     Mr Steve Captain         


     Total                                                                                                390        50.0       18         


     Bowler                                                  Overs      Runs       Wickets    Economy


     Prashanth                                                8          73         1          9.1

     Pruthvi                                                  7          38         2          5.4

     Manoj                                                    9          90         0          10.0

     Eid Mubharak (Cap)                                       8          62         0          7.8

     Gagan                                                    8          76         0          9.5

     Dhinakar                                                 10         51         1          5.1



                                        Golden Green  Won By 43 


==============================================================================================================================================================================


############################################################   MATCH NO -- 2   ############################################################


--------------------::  Innings I  ::------------------

     Batsman                                                                                             Runs       Balls      Sixes      Strike Rate


     Naveen Raja                         Caught  By Veera Raghava                                         24         40         1          60.0

     Eeshwar Jhon                        Stumped By Rambabu Rambo (Wk)                                    51         26         2          196.15

     Shourya Varma (Wk)                  Bowled By Hari Krishna                                           36         25         1          144.0

     Naresh Anthe                        Hit Wicket By Mr Steve Captain                                   83         54         4          153.7

     Harish                              Caught And Bowled By Mr Steve Captain                            8          39         0          20.51

     Prashanth                           Stumped By Rambabu Rambo (Wk)                                    7          23         0          30.43

     Pruthvi                             Stumped By Rambabu Rambo (Wk)                                    71         54         3          131.48

     Manoj                               Stumped By Rambabu Rambo (Wk)                                    71         56         3          126.79

     Eid Mubharak (Cap)        

     Gagan                     

     Dhinakar                  


     Total                                                                                                351        50.0       14         


     Bowler                                                   Overs      Runs       Wickets    Economy


     Wakanda Forevar                                          8          21         0          2.6

     Naveen Chowdary (Cap)                                    8          40         0          5.0

     Hari Krishna                                             8          90         2          11.2

     Veera Raghava                                            8          90         3          11.2

     Mohan Potta                                              9          71         2          7.9

     Mr Steve Captain                                         9          39         1          4.3




------------------:: Innigs II :: ------------

     Batsman                                                                                            Runs       Balls      Sixes      Strike Rate


     Yenugula Harish                     Stumped By Shourya Varma (Wk)                                    74         50         3          148.0

     Jaya Prakash                        Bowled By Gagan                                                  1          40         0          2.5

     Rambabu Rambo (Wk)                  Caught  By Dhinakar                                              93         51         4          182.35

     Rakesh Hulk                         Stumped By Shourya Varma (Wk)                                    32         28         1          114.29

     Raghava PET                         Caught And Bowled By Prashanth                                   99         53         4          186.79

     Wakanda Forevar                     Hit Wicket By Gagan                                              99         56         4          176.79

     Naveen Chowdary (Cap)               Caught And Bowled By Dhinakar                                    12         20         0          60.0

     Hari Krishna                        Bowled By Manoj                                                  50         38         2          131.58

     Veera Raghava            

     Mohan Potta              

     Mr Steve Captain         


     Total                                                                                                460        50.0       18         


     Bowler                                                  Overs      Runs       Wickets    Economy


     Prashanth                                                7          85         2          12.1

     Pruthvi                                                  7          76         2          10.9

     Manoj                                                    8          73         0          9.1

     Eid Mubharak (Cap)                                       10         86         2          8.6

     Gagan                                                    10         54         2          5.4

     Dhinakar                                                 8          86         0          10.8



                                          Billion Dollers Blue   Won By 109


==============================================================================================================================================================================


############################################################   MATCH NO -- 3   ############################################################


--------------------::  Innings I  ::------------------

     Batsman                                                                                             Runs       Balls      Sixes      Strike Rate


     Naveen Raja                         Caught And Bowled By Mr Steve Captain                            33         29         1          113.79

     Eeshwar Jhon                        Stumped By Rambabu Rambo (Wk)                                    4          28         0          14.29

     Shourya Varma (Wk)                  Caught  By Wakanda Forevar                                       110        87         5          126.44

     Naresh Anthe                        Stumped By Rambabu Rambo (Wk)                                    123        83         6          148.19

     Harish                              Bowled By Hari Krishna                                           59         22         2          268.18

     Prashanth                           Stumped By Rambabu Rambo (Wk)                                    37         25         1          148.0

     Pruthvi                             Bowled By Naveen Chowdary (Cap)                                  97         51         4          190.2

     Manoj                     

     Eid Mubharak (Cap)        

     Gagan                     

     Dhinakar                  


     Total                                                                                                463        50.0       19         


     Bowler                                                   Overs      Runs       Wickets    Economy


     Wakanda Forevar                                          8          83         1          10.4

     Naveen Chowdary (Cap)                                    9          90         2          10.0

     Hari Krishna                                             8          90         0          11.2

     Veera Raghava                                            9          45         2          5.0

     Mohan Potta                                              8          82         2          10.2

     Mr Steve Captain                                         8          73         0          9.1




------------------:: Innigs II :: ------------

     Batsman                                                                                            Runs       Balls      Sixes      Strike Rate


     Yenugula Harish                     Caught And Bowled By Pruthvi                                     93         53         4          175.47

     Jaya Prakash                        Caught  By Pruthvi                                               54         39         2          138.46

     Rambabu Rambo (Wk)                  Stumped By Shourya Varma (Wk)                                    43         36         2          119.44

     Rakesh Hulk                         Hit Wicket By Manoj                                              62         55         3          112.73

     Raghava PET                         Bowled By Prashanth                                              118        90         5          131.11

     Wakanda Forevar                     Hit Wicket By Dhinakar                                           115        95         5          121.05

     Naveen Chowdary (Cap)    

     Hari Krishna             

     Veera Raghava            

     Mohan Potta              

     Mr Steve Captain         


     Total                                                                                                485        50.0       21         


     Bowler                                                  Overs      Runs       Wickets    Economy


     Prashanth                                                7          72         1          10.3

     Pruthvi                                                  8          85         0          10.6

     Manoj                                                    7          86         1          12.3

     Eid Mubharak (Cap)                                       10         80         2          8.0

     Gagan                                                    8          72         0          9.0

     Dhinakar                                                 10         90         2          9.0



                                          Billion Dollers Blue   Won By 22


==============================================================================================================================================================================


############################################################   MATCH NO -- 4   ############################################################


--------------------::  Innings I  ::------------------

     Batsman                                                                                             Runs       Balls      Sixes      Strike Rate


     Naveen Raja                         Stumped By Rambabu Rambo (Wk)                                    17         21         0          80.95

     Eeshwar Jhon                        Caught  By Mohan Potta                                           34         25         1          136.0

     Shourya Varma (Wk)                  Caught  By Naveen Chowdary (Cap)                                 124        88         6          140.91

     Naresh Anthe                        Bowled By Hari Krishna                                           112        81         5          138.27

     Harish                              Hit Wicket By Naveen Chowdary (Cap)                              12         32         0          37.5

     Prashanth                           Hit Wicket By Wakanda Forevar                                    91         56         4          162.5

     Pruthvi                   

     Manoj                     

     Eid Mubharak (Cap)        

     Gagan                     

     Dhinakar                  


     Total                                                                                                390        50.0       16         


     Bowler                                                   Overs      Runs       Wickets    Economy


     Wakanda Forevar                                          9          66         1          7.3

     Naveen Chowdary (Cap)                                    8          90         1          11.2

     Hari Krishna                                             9          80         1          8.9

     Veera Raghava                                            8          66         0          8.2

     Mohan Potta                                              8          38         2          4.8

     Mr Steve Captain                                         8          50         1          6.2




------------------:: Innigs II :: ------------

     Batsman                                                                                            Runs       Balls      Sixes      Strike Rate


     Yenugula Harish                     Caught And Bowled By Pruthvi                                     25         28         1          89.29

     Jaya Prakash                        Bowled By Eid Mubharak (Cap)                                     27         31         1          87.1

     Rambabu Rambo (Wk)                  Caught  By Gagan                                                 56         29         2          193.1

     Rakesh Hulk                         Stumped By Shourya Varma (Wk)                                    65         51         3          127.45

     Raghava PET                         Hit Wicket By Dhinakar                                           102        88         5          115.91

     Wakanda Forevar                     Caught  By Harish                                                57         36         2          158.33

     Naveen Chowdary (Cap)               Stumped By Shourya Varma (Wk)                                    110        91         5          120.88

     Hari Krishna             

     Veera Raghava            

     Mohan Potta              

     Mr Steve Captain         


     Total                                                                                                442        50.0       19         


     Bowler                                                  Overs      Runs       Wickets    Economy


     Prashanth                                                8          64         0          8.0

     Pruthvi                                                  10         84         2          8.4

     Manoj                                                    8          80         2          10.0

     Eid Mubharak (Cap)                                       9          81         0          9.0

     Gagan                                                    8          52         1          6.5

     Dhinakar                                                 7          81         2          11.6



                                          Billion Dollers Blue   Won By 52


==============================================================================================================================================================================


############################################################   MATCH NO -- 5   ############################################################


--------------------::  Innings I  ::------------------

     Batsman                                                                                             Runs       Balls      Sixes      Strike Rate


     Naveen Raja                         Bowled By Veera Raghava                                          73         50         3          146.0

     Eeshwar Jhon                        Stumped By Rambabu Rambo (Wk)                                    79         50         3          158.0

     Shourya Varma (Wk)                  Stumped By Rambabu Rambo (Wk)                                    25         40         1          62.5

     Naresh Anthe                        Hit Wicket By Veera Raghava                                      92         55         4          167.27

     Harish                              Bowled By Hari Krishna                                           82         55         4          149.09

     Prashanth                           Caught  By Raghava PET                                           55         32         2          171.88

     Pruthvi                             Bowled By Mr Steve Captain                                       28         21         1          133.33

     Manoj                     

     Eid Mubharak (Cap)        

     Gagan                     

     Dhinakar                  


     Total                                                                                                434        50.0       18         


     Bowler                                                   Overs      Runs       Wickets    Economy


     Wakanda Forevar                                          8          69         0          8.6

     Naveen Chowdary (Cap)                                    9          73         3          8.1

     Hari Krishna                                             8          67         2          8.4

     Veera Raghava                                            9          86         1          9.6

     Mohan Potta                                              8          70         0          8.8

     Mr Steve Captain                                         8          69         1          8.6




------------------:: Innigs II :: ------------

     Batsman                                                                                            Runs       Balls      Sixes      Strike Rate


     Yenugula Harish                     Caught  By Eeshwar Jhon                                          76         51         3          149.02

     Jaya Prakash                        Hit Wicket By Dhinakar                                           10         30         0          33.33

     Rambabu Rambo (Wk)                  Bowled By Dhinakar                                               14         29         0          48.28

     Rakesh Hulk                         Caught And Bowled By Pruthvi                                     100        56         5          178.57

     Raghava PET                         Stumped By Shourya Varma (Wk)                                    36         35         1          102.86

     Wakanda Forevar                     Stumped By Shourya Varma (Wk)                                    58         37         2          156.76

     Naveen Chowdary (Cap)               Caught And Bowled By Dhinakar                                    40         35         2          114.29

     Hari Krishna                        Caught And Bowled By Dhinakar                                    125        99         6          126.26

     Veera Raghava            

     Mohan Potta              

     Mr Steve Captain         


     Total                                                                                                459        50.0       19         


     Bowler                                                  Overs      Runs       Wickets    Economy


     Prashanth                                                8          90         1          11.2

     Pruthvi                                                  10         77         2          7.7

     Manoj                                                    8          71         1          8.9

     Eid Mubharak (Cap)                                       8          70         0          8.8

     Gagan                                                    7          89         2          12.7

     Dhinakar                                                 9          62         2          6.9



                                          Billion Dollers Blue   Won By 25


==============================================================================================================================================================================


 Batsman                             Innings         Runs     Balls     Sixes     Strike Rate Average  

Naveen Raja                          5               186       173       6         107.51    

Eeshwar Jhon                         5               224       149       8         150.34    

Shourya Varma (Wk)                   5               392       296       17        132.43    

Naresh Anthe                         5               463       307       21        150.81    

Harish                               5               190       175       7         108.57    

Prashanth                            5               207       160       7         129.38    

Pruthvi                              4               200       151       8         132.45    

Manoj                                2               89        87        3         102.3     

Eid Mubharak (Cap)                   1               120       87        6         137.93    

Gagan                                0               0         0         0          0         

Dhinakar                             0               0         0         0          0         




 Batsman                             Innings         Runs     Balls     Sixes     Strike Rate

Yenugula Harish                      5               372       273       16        136.26   

Jaya Prakash                         5               166       194       6         85.57    

Rambabu Rambo (Wk)                   5               308       231       13        133.33   

Rakesh Hulk                          5               369       278       17        132.73   

Raghava PET                          4               355       266       15        133.46   

Wakanda Forevar                      4               329       224       13        146.88   

Naveen Chowdary (Cap)                3               162       146       7         110.96   

Hari Krishna                         2               175       137       8         127.74   

Veera Raghava                        0               0         0         0          0         

Mohan Potta                          0               0         0         0          0         

Mr Steve Captain                     0               0         0         0          0         


Process finished with exit code 0


"""


