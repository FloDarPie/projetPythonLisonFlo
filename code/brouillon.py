import tkinter as tk
from PIL import Image, ImageTk
#importer PIL permet d'utilsier des images autres que gif
 
#fonction permettant de créer une fenêtre contenant notre image
def fen1():
     
    top = tk.Toplevel(master=fenetre, background='red') #création d'une 2e fenetre qui
                                                        #fonctionne sous le meme mainloop()
                                                        #que la fenetre principale (fenetre)
    image = Image.open("C:\Documents and Settings\philippe.noel\Bureau\\test.JPG")
    photo = ImageTk.PhotoImage(image) #ouverture de l'image avec PIL et convertion pour Tkinter
 
     
    can = tk.Canvas(top, width = image.size[0], height = image.size[1]) #création du canevas qui va contenir la photo
    can.create_image(0,0,anchor = tk.NW, image=photo)
    can.image=photo #Attention reference a ne pas oublier afin de conserver l'image et qu'elle soit bien affichée
    can.pack()
    button = tk.Button(top, text="quitter", command=top.destroy)
    button.pack()
 
 
###initialisation de tkinter###
     
fenetre= tk.Tk()
bouton = tk.Button(fenetre,text='afficher_image',command=fen1)
bouton.pack(side=tk.LEFT)
fenetre.mainloop()
