from simplex import *
from screen import *

if __name__ == "__main__":
    #iniciando a tela
    root = Tk()
    width= root.winfo_screenwidth()  
    height= root.winfo_screenheight() 
    root.geometry("%dx%d" % (width, height)) 
    root.state(newstate="zoomed")
    root.title('Método Simplex')
    Application(root)
    root.mainloop()