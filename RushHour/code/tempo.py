information = information_niveau_precis(1)
        ligne = lecture_ligne(1)

        if ligne[0]=="F":
            tk.Button(popup, text="Niveau : "+str(1), bg = "darkgoldenrod", activebackground=information[2], height = 2, width=10, command=lambda:[popup.destroy(),  change_niveau(1), self.fenetre()], font=f).place(x =  10, y= 10)
        else:
            tk.Button(popup, text="Niveau : "+str(1), bg = "black", activebackground="black", height = 2, width=10, font=f).place(x= 10, y= 10)
            
        information = information_niveau_precis(2)
        ligne = lecture_ligne(2)

        if ligne[0]=="F":
            tk.Button(popup, text="Niveau : "+str(2), bg = "darkgoldenrod", activebackground=information[2], height = 2, width=10, command=lambda:[popup.destroy(),  change_niveau(2), self.fenetre()], font=f).place(x =  160, y= 10)
        else:
            tk.Button(popup, text="Niveau : "+str(2), bg = "black", activebackground="black", height = 2, width=10, font=f).place(x= 160, y= 10)
            
        information = information_niveau_precis(3)
        ligne = lecture_ligne(3)

        if ligne[0]=="F":
            tk.Button(popup, text="Niveau : "+str(3), bg = "darkgoldenrod", activebackground=information[2], height = 2, width=10, command=lambda:[popup.destroy(),  change_niveau(3), self.fenetre()], font=f).place(x =  310, y= 10)
        else:
            tk.Button(popup, text="Niveau : "+str(3), bg = "black", activebackground="black", height = 2, width=10, font=f).place(x= 310, y= 10)

        information = information_niveau_precis(4)
        ligne = lecture_ligne(4)

        if ligne[0]=="F":
            tk.Button(popup, text="Niveau : "+str(4), bg = "darkgoldenrod", activebackground=information[2], height = 2, width=10, command=lambda:[popup.destroy(),  change_niveau(4), self.fenetre()], font=f).place(x =  460, y= 10)
        else:
            tk.Button(popup, text="Niveau : "+str(4), bg = "black", activebackground="black", height = 2, width=10, font=f).place(x= 460, y= 10)

        information = information_niveau_precis(5)
        ligne = lecture_ligne(5)

        if ligne[0]=="F":
            tk.Button(popup, text="Niveau : "+str(5), bg = "darkgoldenrod", activebackground=information[2], height = 2, width=10, command=lambda:[popup.destroy(),  change_niveau(5), self.fenetre()], font=f).place(x =  10, y= 110)
        else:
            tk.Button(popup, text="Niveau : "+str(5), bg = "black", activebackground="black", height = 2, width=10, font=f).place(x= 10, y= 110)

        information = information_niveau_precis(6)
        ligne = lecture_ligne(6)

        if ligne[0]=="F":
            tk.Button(popup, text="Niveau : "+str(6), bg = "darkgoldenrod", activebackground=information[2], height = 2, width=10, command=lambda:[popup.destroy(),  change_niveau(6), self.fenetre()], font=f).place(x =  160, y= 110)
        else:
            tk.Button(popup, text="Niveau : "+str(6), bg = "black", activebackground="black", height = 2, width=10, font=f ).place(x= 160, y= 110)
          
        information = information_niveau_precis(7)
        ligne = lecture_ligne(7)

        if ligne[0]=="F":
            tk.Button(popup, text="Niveau : "+str(7), bg = "darkgoldenrod", activebackground=information[2], height = 2, width=10, command=lambda:[popup.destroy(),  change_niveau(7), self.fenetre()], font=f).place(x =  310, y= 110)
        else:
            tk.Button(popup, text="Niveau : "+str(7), bg = "black", activebackground="black", height = 2, width=10, font=f).place(x= 310, y= 110)
          
        information = information_niveau_precis(8)
        ligne = lecture_ligne(8)

        if ligne[0]=="F":
            tk.Button(popup, text="Niveau : "+str(8), bg = "darkgoldenrod", activebackground=information[2], height = 2, width=10, command=lambda:[popup.destroy(),  change_niveau(8), self.fenetre()], font=f).place(x =  460, y= 110)
        else:
            tk.Button(popup, text="Niveau : "+str(8), bg = "black", activebackground="black", height = 2, width=10, font=f).place(x= 460, y= 110)
          
        information = information_niveau_precis(9)
        ligne = lecture_ligne(9)

        if ligne[0]=="F":
            tk.Button(popup, text="Niveau : "+str(9), bg = "darkgoldenrod", activebackground=information[2], height = 2, width=10, command=lambda:[popup.destroy(),  change_niveau(9), self.fenetre()], font=f).place(x =  10, y= 210)
        else:
            tk.Button(popup, text="Niveau : "+str(9), bg = "black", activebackground="black", height = 2, width=10, font=f).place(x= 10, y= 210)
                    
        information = information_niveau_precis(10)
        ligne = lecture_ligne(10)

        if ligne[0]=="F":
            tk.Button(popup, text="Niveau : "+str(10), bg = "darkgoldenrod", activebackground=information[2], height = 2, width=10, command=lambda:[popup.destroy(),  change_niveau(10), self.fenetre()], font=f).place(x =  160, y= 210)
        else:
            tk.Button(popup, text="Niveau : "+str(10), bg = "black", activebackground="black", height = 2, width=10, font=f).place(x= 160, y= 210)
                    
        information = information_niveau_precis(11)
        ligne = lecture_ligne(11)

        if ligne[0]=="F":
            tk.Button(popup, text="Niveau : "+str(11), bg = "darkgoldenrod", activebackground=information[2], height = 2, width=10, command=lambda:[popup.destroy(),  change_niveau(11), self.fenetre()], font=f).place(x =  310, y= 210)
        else:
            tk.Button(popup, text="Niveau : "+str(11), bg = "black", activebackground="black", height = 2, width=10, font=f).place(x= 310, y= 210)
                    
        information = information_niveau_precis(12)
        ligne = lecture_ligne(12)

        if ligne[0]=="F":
            tk.Button(popup, text="Niveau : "+str(12), bg = "darkgoldenrod", activebackground=information[2], height = 2, width=10, command=lambda:[popup.destroy(),  change_niveau(12), self.fenetre()], font=f).place(x =  460, y= 210)
        else:
            tk.Button(popup, text="Niveau : "+str(12), bg = "black", activebackground="black", height = 2, width=10, font=f).place(x= 460, y= 210)
                    
        information = information_niveau_precis(13)
        ligne = lecture_ligne(13)

        if ligne[0]=="F":
            tk.Button(popup, text="Niveau : "+str(13), bg = "darkgoldenrod", activebackground=information[2], height = 2, width=10, command=lambda:[popup.destroy(),  change_niveau(13), self.fenetre()], font=f).place(x =  10, y= 310)
        else:
            tk.Button(popup, text="Niveau : "+str(13), bg = "black", activebackground="black", height = 2, width=10, font=f).place(x= 10, y= 310)
                    
        information = information_niveau_precis(14)
        ligne = lecture_ligne(14)

        if ligne[0]=="F":
            tk.Button(popup, text="Niveau : "+str(14), bg = "darkgoldenrod", activebackground=information[2], height = 2, width=10, command=lambda:[popup.destroy(),  change_niveau(14), self.fenetre()], font=f).place(x =  160 , y= 310 )
        else:
            tk.Button(popup, text="Niveau : "+str(14), bg = "black", activebackground="black", height = 2, width=10, font=f).place(x= 160 , y= 310 )
                    
        information = information_niveau_precis(15)
        ligne = lecture_ligne(15)

        if ligne[0]=="F":
            tk.Button(popup, text="Niveau : "+str(15), bg = "darkgoldenrod", activebackground=information[2], height = 2, width=10, command=lambda:[popup.destroy(),  change_niveau(15), self.fenetre()], font=f).place(x =  310 , y= 310 )
        else:
            tk.Button(popup, text="Niveau : "+str(15), bg = "black", activebackground="black", height = 2, width=10, font=f).place(x= 310 , y= 310 )
                
        information = information_niveau_precis(16)
        ligne = lecture_ligne(16)

        if ligne[0]=="F":
            tk.Button(popup, text="Niveau : "+str(16), bg = "darkgoldenrod", activebackground=information[2], height = 2, width=10, command=lambda:[popup.destroy(),  change_niveau(16), self.fenetre()], font=f).place(x =  460 , y= 310 )
        else:
            tk.Button(popup, text="Niveau : "+str(16), bg = "black", activebackground="black", height = 2, width=10, font=f).place(x= 460 , y= 310 )
            
        information = information_niveau_precis(17)
        ligne = lecture_ligne(17)

        if ligne[0]=="F":
            tk.Button(popup, text="Niveau : "+str(17), bg = "darkgoldenrod", activebackground=information[2], height = 2, width=10, command=lambda:[popup.destroy(),  change_niveau(17), self.fenetre()], font=f).place(x =  10 , y= 410 )
        else:
            tk.Button(popup, text="Niveau : "+str(17), bg = "black", activebackground="black", height = 2, width=10, font=f).place(x= 10 , y= 410 )
            
        information = information_niveau_precis(18)
        ligne = lecture_ligne(18)

        if ligne[0]=="F":
            tk.Button(popup, text="Niveau : "+str(18), bg = "darkgoldenrod", activebackground=information[2], height = 2, width=10, command=lambda:[popup.destroy(),  change_niveau(18), self.fenetre()], font=f).place(x =  160 , y= 410 )
        else:
            tk.Button(popup, text="Niveau : "+str(18), bg = "black", activebackground="black", height = 2, width=10, font=f).place(x= 160 , y= 410 )
            
        information = information_niveau_precis(19)
        ligne = lecture_ligne(19)

        if ligne[0]=="F":
            tk.Button(popup, text="Niveau : "+str(19), bg = "darkgoldenrod", activebackground=information[2], height = 2, width=10, command=lambda:[popup.destroy(),  change_niveau(19), self.fenetre()], font=f).place(x =  310 , y= 410 )
        else:
            tk.Button(popup, text="Niveau : "+str(19), bg = "black", activebackground="black", height = 2, width=10, font=f).place(x= 310 , y= 410 )
            
        information = information_niveau_precis(20)
        ligne = lecture_ligne(20)

        if ligne[0]=="F":
            tk.Button(popup, text="Niveau : "+str(20), bg = "darkgoldenrod", activebackground=information[2], height = 2, width=10, command=lambda:[popup.destroy(),  change_niveau(20), self.fenetre()], font=f).place(x =  460 , y= 410 )
        else:
            tk.Button(popup, text="Niveau : "+str(20), bg = "black", activebackground="black", height = 2, width=10, font=f).place(x= 460 , y= 410 )

        
