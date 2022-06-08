import scalcu as stat
import evcalcu as eval
def otherStat():
    
    print("For Other Stat Calculation\n")
    opt = int(input("Choose what other stat you want to view: \n1. Attack\n2. Defense\n3.Speed \n4.Sp. Attack\n5.Sp. Defense\n"))
    #attack stat
    if opt == 1:
        base_os = int(input("Input Base Hp Stat: "))
        Iv_os = int(input("Input Initial Values Between 0 to 31: "))
        if Iv_os<0 or Iv_os>31:
            print("Your inputted value is out of range!")
            otherStat()
        Ev_os = int(input("Input Effort Value Between 0 to 255:"))
        if Ev_os<0 or Ev_os>255:
            print("Your inputted value is out of range!")
            otherStat()
        level1 = int(input("Enter the target level pokemon"))
        nature = int(input("""Pick a Nature
        0. Hardy 1. Lonely 2. Brave 3. Adamant 4. Naughty 5. Bold
        6. Docile 7. Relaxed 8. Implish 9. Lax 10. Timid
        11. Hasty 12. Serious 13. Jolly 14. Naive 15. Modest
        16. Mild 17. Quiet 18. Bashful 19. Rash 20. Calm
        21. Gentle 22. Sassy 23. Careful 24. Quirky\n """))

        if nature == 1 and 2 and 3 and 4:
            total1 = stat.scalc.attackb(base_os,Iv_os,Ev_os,level1)
            print("The total other stat attack is : ",total1)
    
        elif nature == 5 and 10 and 15 and 20:
            total1 = stat.scalc.attackh(base_os,Iv_os,Ev_os,level1)
            print("The total other stat attack is : ",total1)
    
        else:
            total1 = stat.scalc.attackn(base_os,Iv_os,Ev_os,level1)
            print("The total other stat attack is : ",total1,)

    #defense stat
    elif opt == 2:
        base_os = int(input("Input Base Hp Stat: "))
        Iv_os = int(input("Input Initial Values Between 0 to 31: "))
        if Iv_os<0 or Iv_os>31:
            print("Your inputted value is out of range!")
            otherStat()
        Ev_os = int(input("Input Effort Value Between 0 to 255:"))
        if Ev_os<0 or Ev_os>255:
            print("Your inputted value is out of range!")
            otherStat()
        level1 = int(input("Enter the target level pokemon"))
        nature = int(input("""Pick a Nature
        0. Hardy 1. Lonely 2. Brave 3. Adamant 4. Naughty 5. Bold
        6. Docile 7. Relaxed 8. Implish 9. Lax 10. Timid
        11. Hasty 12. Serious 13. Jolly 14. Naive 15. Modest
        16. Mild 17. Quiet 18. Bashful 19. Rash 20. Calm
        21. Gentle 22. Sassy 23. Careful 24. Quirky\n """))

        if nature == 5 and 7 and 8 and 9:
            total1 = stat.scalc.defenseb(base_os,Iv_os,Ev_os,level1)
            print("The total other stat defense is : ",total1)
    
        elif nature == 1 and 11 and 16 and 21:
            total1 = stat.scalc.defenseh(base_os,Iv_os,Ev_os,level1)
            print("The total other stat defense is : ",total1)
    
        else:
            total1 = stat.scalc.defensen(base_os,Iv_os,Ev_os,level1)
            print("The total other stat defense is : ",total1,)
    
    #speed stat
    elif opt == 3:
        base_os = int(input("Input Base Hp Stat: "))
        Iv_os = int(input("Input Initial Values Between 0 to 31: "))
        if Iv_os<0 or Iv_os>31:
            print("Your inputted value is out of range!")
            otherStat()
        Ev_os = int(input("Input Effort Value Between 0 to 255:"))
        if Ev_os<0 or Ev_os>255:
            print("Your inputted value is out of range!")
            otherStat()
        level1 = int(input("Enter the target level pokemon"))
        nature = int(input("""Pick a Nature
        0. Hardy 1. Lonely 2. Brave 3. Adamant 4. Naughty 5. Bold
        6. Docile 7. Relaxed 8. Implish 9. Lax 10. Timid
        11. Hasty 12. Serious 13. Jolly 14. Naive 15. Modest
        16. Mild 17. Quiet 18. Bashful 19. Rash 20. Calm
        21. Gentle 22. Sassy 23. Careful 24. Quirky\n """))

        if nature == 10 and 11 and 13 and 14:
            total1 = stat.scalc.speedb(base_os,Iv_os,Ev_os,level1)
            print("The total other stat speed is : ",total1)
    
        elif nature == 2 and 7 and 17 and 22:
            total1 = stat.scalc.speedh(base_os,Iv_os,Ev_os,level1)
            print("The total other stat speed is : ",total1)
    
        else:
            total1 = stat.scalc.speedn(base_os,Iv_os,Ev_os,level1)
            print("The total other stat speed is : ",total1,)
    
    #sp.atk stat
    elif opt == 4:
        base_os = int(input("Input Base Hp Stat: "))
        Iv_os = int(input("Input Initial Values Between 0 to 31: "))
        if Iv_os<0 or Iv_os>31:
            print("Your inputted value is out of range!")
            otherStat()
        Ev_os = int(input("Input Effort Value Between 0 to 255:"))
        if Ev_os<0 or Ev_os>255:
            print("Your inputted value is out of range!")
            otherStat()
        level1 = int(input("Enter the target level pokemon"))
        nature = int(input("""Pick a Nature
        0. Hardy 1. Lonely 2. Brave 3. Adamant 4. Naughty 5. Bold
        6. Docile 7. Relaxed 8. Implish 9. Lax 10. Timid
        11. Hasty 12. Serious 13. Jolly 14. Naive 15. Modest
        16. Mild 17. Quiet 18. Bashful 19. Rash 20. Calm
        21. Gentle 22. Sassy 23. Careful 24. Quirky\n """))

        if nature == 15 and 16 and 17 and 19:
            total1 = stat.scalc.sptkb(base_os,Iv_os,Ev_os,level1)
            print("The total other stat speed is : ",total1)
    
        elif nature == 3 and 8 and 13 and 23:
            total1 = stat.scalc.sptkh(base_os,Iv_os,Ev_os,level1)
            print("The total other stat speed is : ",total1)
    
        else:
            total1 = stat.scalc.sptkn(base_os,Iv_os,Ev_os,level1)
            print("The total other stat speed is : ",total1,)
    
    #sp.def stat
    elif opt == 5:
        base_os = int(input("Input Base Hp Stat: "))
        Iv_os = int(input("Input Initial Values Between 0 to 31: "))
        if Iv_os<0 or Iv_os>31:
            print("Your inputted value is out of range!")
            otherStat()
        Ev_os = int(input("Input Effort Value Between 0 to 255:"))
        if Ev_os<0 or Ev_os>255:
            print("Your inputted value is out of range!")
            otherStat()
        level1 = int(input("Enter the target level pokemon"))
        nature = int(input("""Pick a Nature
        0. Hardy 1. Lonely 2. Brave 3. Adamant 4. Naughty 5. Bold
        6. Docile 7. Relaxed 8. Implish 9. Lax 10. Timid
        11. Hasty 12. Serious 13. Jolly 14. Naive 15. Modest
        16. Mild 17. Quiet 18. Bashful 19. Rash 20. Calm
        21. Gentle 22. Sassy 23. Careful 24. Quirky\n """))

        if nature == 20 and 21 and 22 and 23:
            total1 = stat.scalc.spdeb(base_os,Iv_os,Ev_os,level1)
            print("The total other stat speed is : ",total1)
    
        elif nature == 4 and 9 and 14 and 19:
            total1 = stat.scalc.spdeh(base_os,Iv_os,Ev_os,level1)
            print("The total other stat speed is : ",total1)
    
        else:
            total1 = stat.scalc.spden(base_os,Iv_os,Ev_os,level1)
            print("The total other stat speed is : ",total1,)
    
    else:
        print("Invalid Input!")
        otherStat()
    

def main():
    print("Choose an Option: ")
    user = int(input("1. Stat\n2. EV\n=> "))
    if user == 1:
        base = int(input("Input base hp stat: "))
        Iv = int(input("Input Initial Value Between 0 to 31: "))
        if Iv<0 or Iv>31:
            print("Your inputted value is out of range!")
            main()
        
        Ev = int(input("Input Effort Value Between 0 to 255: "))
        if Ev<0 or Ev>255:
            print("Your inputted value is out of range!")
            main()
        level = int(input("Enter the target level of pokemon: "))
        print("Your base hp is",base,"\nInitial Value",Iv,"\nEffort Value",Ev,"\nTarget Level of Pokemon is",level)
        total = stat.scalc.health(base,Iv,Ev,level)
        print("The Pokemon Hp Stat Value is", total)
        os = int(input("You want to see other Stat? \n1.Yes \n2. No"))
        if os == 1:
            otherStat()
        
        elif os == 2:
            main()
        
        else:
            print("Invalid Input!")


    
    elif user == 2:
        ev_stats = int(input("Enter the desired increased in stat: "))
        target = int(input("Enter the target level of Pokemon: "))
        base_stats = int(input("Input Base Stat: "))
        IV = int(input("Enter Individual Value: "))
        if IV<0 or IV>31:
            print("Your inputted value is out of range!")
            main()
        EV = int(input("Enter Effort Value: "))
        if EV<0 or EV>255:
            print("Your inputted value is out of range!")
            main()
        mods = int(input("Input what kind of Nature: \n1. Beneficial \n2.Hindering\n=>"))
        if mods == 1:
            mods = 1.1
        elif mods ==2:
            mods = 0.9
        else:
            print("Invalid Input")
            main()
        D = EV/4
        D = (2*base_stats+IV+D)
        D = D*(target/100)
        total2 = eval.evcalc.Evs(ev_stats,mods,D,target)
        print("Evs Needed: ",total2)
        main()


main()