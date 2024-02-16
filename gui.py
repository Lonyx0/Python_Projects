from tkinter import *
from tkcalendar import DateEntry
from tkinter import messagebox

def gonder():
    son_mesaj= ""
    try:
        if var.get():
            if var.get() == 1:
                son_mesaj += "Veriniz basariyla sisteme kaydedilmistir"

                tip = hatirlatma_tipi_opsiyon.get() if hatirlatma_tipi_opsiyon=='' else "Genel"
                tarih = hatirlatma_tarih_secici.get()
                mesaj = metin_alani.get("1.0", "end")

                with open("hatirlatmalar.txt","w") as dosya:
                    dosya.write('{} kategorisinde,{} tarihine ve "{}" notuyla hatirlatma'.format(tip,tarih,mesaj))
                    dosya.close()


            elif var.get() == 2:
                son_mesaj += "E posta yoluyla hatirlatma size ulasacaktir"
            
            messagebox.showinfo("Basarili islem", son_mesaj)
        
        else:
            son_mesaj += "Gerekli alanlarin dolduruldugundan emin olun..."
            messagebox.showwarning("Yetersiz Bilgi",son_mesaj)
    except:
        son_mesaj += "Islem Basarisiz Oldu!"
        messagebox.showerror("Basarisiz Islem",son_mesaj)

    finally:
        master.destroy()


master = Tk()

canvas = Canvas(master, height=450, width=750)
canvas.pack()

frame_ust = Frame(master, bg='#add8e6')
frame_ust.place(relx=0.1,rely=0.1, relwidth=0.8,relheight=0.1)

frame_alt_sol = Frame(master, bg='#add8e6')
frame_alt_sol.place(relx=0.1,rely=0.21,relwidth=0.23,relheight=0.5)

frame_alt_sag = Frame(master, bg='#add8e6')
frame_alt_sag.place(relx=0.34,rely=0.21,relwidth=0.56,relheight=0.5)

hatirlatma_tipi_etiket = Label(frame_ust, bg='#add8e6',text="Hatirlatma Tipi", font="Verdana 12 bold")
hatirlatma_tipi_etiket.pack(padx=10,pady=10, side=LEFT)

hatirlatma_tipi_opsiyon = StringVar(frame_ust)
hatirlatma_tipi_opsiyon.set("\t")

hatirlatma_tipi_acilir_menu = OptionMenu(frame_ust,hatirlatma_tipi_opsiyon,"Dogum günü","Alisveris","Ödeme")
hatirlatma_tipi_acilir_menu.pack(padx=10,pady=10, side=LEFT)

hatirlatma_tarih_secici = DateEntry(frame_ust, width=12, background = 'orange',foreground='black',locals="tr_TR")
hatirlatma_tarih_secici._top_cal.overrideredirect(False)
hatirlatma_tarih_secici.pack(padx=10,pady=10, side=RIGHT)

hatirlatma_tarihi_etiket = Label(frame_ust, bg='#add8e6',text="Hatirlatma Tarihi", font="Verdana 12 bold")
hatirlatma_tarihi_etiket.pack(padx=10,pady=10, side=RIGHT)

Label(frame_alt_sol,text="Hatirlatma Yöntemi",bg='#add8e6',font="Verdana 10 bold").pack(padx=10,pady=10,anchor=NW)

var = IntVar()
R1 = Radiobutton(frame_alt_sol, text="Sisteme Kaydet", variable= var,value=1,bg='#add8e6',font="Verdana 8")
R1.pack(anchor=NW,pady=5,padx=15)

R2 = Radiobutton(frame_alt_sol, text="E-Posta Gönder", variable= var,value=2,bg='#add8e6',font="Verdana 8")
R2.pack(anchor=NW,pady=5,padx=15)

var1= IntVar()
C1 = Checkbutton(frame_alt_sol, text="Bir Hafta Önce",variable=var1,onvalue=1,offvalue=0,bg='#add8e6',font="Verdana 8")
C1.pack(anchor=NW,pady=2,padx=25)

var2= IntVar()
C2 = Checkbutton(frame_alt_sol, text="Bir Gün Önce",variable=var2,onvalue=1,offvalue=0,bg='#add8e6',font="Verdana 8")
C2.pack(anchor=NW,pady=2,padx=25)

var3= IntVar()
C3 = Checkbutton(frame_alt_sol, text="Ayni Gün",variable=var3,onvalue=1,offvalue=0,bg='#add8e6',font="Verdana 8")
C3.pack(anchor=NW,pady=2,padx=25)

Label(frame_alt_sag, text="Hatirlatma Mesaji",bg='#add8e6',font="Verdana 10 bold").pack(anchor=NW,padx=10,pady=10)

metin_alani = Text(frame_alt_sag,height= 9,width=50)
metin_alani.tag_configure('style',foreground='#bfbfbf',font=('Verdana',7,'bold'))
metin_alani.pack()

karsilama_metni= 'Mesajini Buraya Gir...'
metin_alani.insert(END,karsilama_metni,'style')

gonder_butonu = Button(frame_alt_sag, text="Gönder",command=gonder)
gonder_butonu.pack(anchor=S)


master.mainloop()
