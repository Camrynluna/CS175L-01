#CS175L-01
#Camryn Moschitta

#world_series

continuing='yes'
while continuing=='yes' or continuing=='Yes' or continuing=='YES':
    team=str(input('Enter the name of a team: '))
    with open('WorldSeriesWinners.txt','r') as file:
        count=0
        lines=file.readlines()
        for line in lines:
            line=line.rstrip('\n')
            if team.lower() == line.lower():
                count += 1
        print(f'The {team} won the the world series {count} times between 1903 and 2009')
        continuing=str(input('Would you like to continue?: '))         
