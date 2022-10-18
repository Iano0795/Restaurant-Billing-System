import tkinter as tk
import sys
import tkinter.messagebox as mb
import random

window = tk.Tk()
def hideEverything():
    Frame_Top.place_forget()
    Frame_bottom.place_forget()
    Title.place_forget()
    TOTAL.place_forget()
    RECEIPT.place_forget()
    RESET.place_forget()
    EXIT.place_forget()
    Button_0.place_forget()
    Button_1.place_forget()
    Button_2.place_forget()
    Button_3.place_forget()
    Button_4.place_forget()
    Button_5.place_forget()
    Button_6.place_forget()
    Button_7.place_forget()
    Button_8.place_forget()
    Button_9.place_forget()
    Button_equal.place_forget()
    Button_c.place_forget()
    Button_minus.place_forget()
    Button_multi.place_forget()
    Button_div.place_forget()
    Button_plus.place_forget()
    Button_dot.place_forget()



def main():
    hideEverything()
    Latte_Entry.insert("end", "0")
    Espresso_Entry.insert("end", "0")
    Iced_latte_Entry.insert("end", "0")
    SexOn_Entry.insert("end", "0")
    Cappucino_Entry.insert("end", "0")
    Frappé_Entry.insert("end", "0")
    Doppio_Entry.insert("end", "0")
    Iced_cap_Entry.insert("end", "0")
    Mojito_Entry.insert("end", "0")
    Cheese_Entry.insert("end", "0")
    Red_Entry.insert("end", "0")
    Pasta_Entry.insert("end", "0")
    lasagna_Entry.insert("end", "0")
    Carnitas_Entry.insert("end", "0")
    Cheeseburger_Entry.insert("end", "0")
    Layered_Entry.insert("end", "0")
    choc_Entry.insert("end", "0")
    Reuben_Entry.insert("end", "0")
    listbox_Drinks.insert("end", "0")
    listbox_Cakes.insert("end", "0")
    listbox_Charge.insert("end", "0")
    Tax_Listbox.insert("end", "0")
    Sub_Listbox.insert("end", "0")
    Total_Listbox.insert("end", "0")
    Cash_Entry.insert("end", "0")
    listbox_Remain.insert("end", "0")

    Latte_Entry.config(state="disabled")
    Reuben_Entry.config(state="disabled")
    choc_Entry.config(state="disabled")
    Layered_Entry.config(state="disabled")
    Cheeseburger_Entry.config(state="disabled")
    Carnitas_Entry.config(state="disabled")
    lasagna_Entry.config(state="disabled")
    Pasta_Entry.config(state="disabled")
    Red_Entry.config(state="disabled")
    Cheese_Entry.config(state="disabled")
    Mojito_Entry.config(state="disabled")
    Iced_cap_Entry.config(state="disabled")
    Doppio_Entry.config(state="disabled")
    Frappé_Entry.config(state="disabled")
    Cappucino_Entry.config(state="disabled")
    SexOn_Entry.config(state="disabled")
    Iced_latte_Entry.config(state="disabled")
    Espresso_Entry.config(state="disabled")

    listbox.insert("end", "=================================================")
    listbox.insert("end", "               RESTAURANT BILLING SYSTEM")
    listbox.insert("end", "=================================================")

    window.mainloop()

def adminLogin():
    admin.place_forget()
    staff.place_forget()
    userName.place(relx=0.1,rely=0.08)
    userName_entry.place(relx=0.4,rely=0.08)
    password.place(relx=0.1,rely=0.4)
    passwd_entry.place(relx=0.4,rely=0.4)
    userName.config(text="Manager account")
    back_button.place(relx=0.05,rely=0.85)
    login_button.place(relx=0.83,rely=0.85)

def staffLogin():
    admin.place_forget()
    staff.place_forget()
    userName.place(relx=0.1,rely=0.08)
    userName_entry.place(relx=0.4,rely=0.08)
    password.place(relx=0.1,rely=0.4)
    passwd_entry.place(relx=0.4,rely=0.4)
    userName.config(text="Staff account")
    back_button.place(relx=0.05,rely=0.85)
    login_button.place(relx=0.83,rely=0.85)

def backbtn():
    admin.place(relx=0.3,rely=0.1)
    staff.place(relx=0.35,rely=0.4)
    userName.place_forget()
    userName_entry.place_forget()
    password.place_forget()
    passwd_entry.place_forget()
    userName_entry.delete(0,tk.END)
    passwd_entry.delete(0,tk.END)
    back_button.place_forget()
    login_button.place_forget()

def Login():
    if userName_entry.get() != "" and passwd_entry.get() != "":
        welcome.place_forget()
        login_frame.place_forget()
        Frame_Top.place(relx=0, rely=0.003, relheight=1, relwidth=1)
        Frame_bottom.place(relx=0, rely=0.72, relheight=0.28, relwidth=0.7)
        Title.place(relx=0.004, rely=0.01, relheight=0.08, width=1353)
        TOTAL.place(relx=0.699, rely=0.92, height=45, width=100)
        RECEIPT.place(relx=0.773, rely=0.92, height=45, width=100)
        RESET.place(relx=0.848, rely=0.92, height=45, width=100)
        EXIT.place(relx=0.92, rely=0.92, height=45, width=100)
        Button_0.place(relx=0.70, rely=0.368, height=45, width=100)
        Button_1.place(relx=0.70, rely=0.3, height=45, width=100)
        Button_2.place(relx=0.774, rely=0.3, height=45, width=100)
        Button_3.place(relx=0.847, rely=0.3, height=45, width=100)
        Button_4.place(relx=0.70, rely=0.235, height=45, width=100)
        Button_5.place(relx=0.774, rely=0.235, height=45, width=100)
        Button_6.place(relx=0.847, rely=0.235, height=45, width=100)
        Button_7.place(relx=0.70, rely=0.17, height=45, width=100)
        Button_8.place(relx=0.774, rely=0.17, height=45, width=100)
        Button_9.place(relx=0.847, rely=0.17, height=45, width=100)
        Button_equal.place(relx=0.847, rely=0.368, height=45, width=100)
        Button_c.place(relx=0.92, rely=0.105, height=45, width=100)
        Button_minus.place(relx=0.92, rely=0.235, height=45, width=100)
        Button_multi.place(relx=0.92, rely=0.3, height=45, width=100)
        Button_div.place(relx=0.92, rely=0.368, height=45, width=100)
        Button_plus.place(relx=0.92, rely=0.17, height=45, width=100)
        Button_dot.place(relx=0.774, rely=0.368, height=45, width=100)
    else:
        mb.showwarning("warning","Please fill the inputs")

def reset():
    m = mb.askyesno("SYSTEM ALERT", "Are You Sure Reset All..! \n")

    if m == 1:
        Latte_Entry.delete(0, 5)
        Espresso_Entry.delete(0, 5)
        Iced_latte_Entry.delete(0, 5)
        SexOn_Entry.delete(0, 5)
        Cappucino_Entry.delete(0, 5)
        Frappé_Entry.delete(0, 5)
        Doppio_Entry.delete(0, 5)
        Iced_cap_Entry.delete(0, 5)
        Mojito_Entry.delete(0, 5)
        Cheese_Entry.delete(0, 5)
        Red_Entry.delete(0, 5)
        Pasta_Entry.delete(0, 5)
        lasagna_Entry.delete(0, 5)
        Carnitas_Entry.delete(0, 5)
        Cheeseburger_Entry.delete(0, 5)
        Layered_Entry.delete(0, 5)
        choc_Entry.delete(0, 5)
        Reuben_Entry.delete(0, 5)
        listbox_Drinks.delete(0, 5)
        listbox_Cakes.delete(0, 5)
        listbox_Charge.delete(0, 5)
        Tax_Listbox.delete(0, 5)
        Sub_Listbox.delete(0, 5)
        Total_Listbox.delete(0, 5)
        Cash_Entry.delete(0, 5)
        listbox_Remain.delete(0, 5)
        Entry_Cal.delete(0, 10)

        Latte_Entry.insert("end", "0")
        Espresso_Entry.insert("end", "0")
        Iced_latte_Entry.insert("end", "0")
        SexOn_Entry.insert("end", "0")
        Cappucino_Entry.insert("end", "0")
        Frappé_Entry.insert("end", "0")
        Doppio_Entry.insert("end", "0")
        Iced_cap_Entry.insert("end", "0")
        Mojito_Entry.insert("end", "0")
        Cheese_Entry.insert("end", "0")
        Red_Entry.insert("end", "0")
        Pasta_Entry.insert("end", "0")
        lasagna_Entry.insert("end", "0")
        Carnitas_Entry.insert("end", "0")
        Cheeseburger_Entry.insert("end", "0")
        Layered_Entry.insert("end", "0")
        choc_Entry.insert("end", "0")
        Reuben_Entry.insert("end", "0")
        listbox_Drinks.insert("end", "0")
        listbox_Cakes.insert("end", "0")
        listbox_Charge.insert("end", "0")
        Tax_Listbox.insert("end", "0")
        Sub_Listbox.insert("end", "0")
        Total_Listbox.insert("end", "0")
        Cash_Entry.insert("end", "0")
        listbox_Remain.insert("end", "0")

        Latte_Entry.config(state="disabled")
        Reuben_Entry.config(state="disabled")
        choc_Entry.config(state="disabled")
        Layered_Entry.config(state="disabled")
        Cheeseburger_Entry.config(state="disabled")
        Carnitas_Entry.config(state="disabled")
        lasagna_Entry.config(state="disabled")
        Pasta_Entry.config(state="disabled")
        Red_Entry.config(state="disabled")
        Cheese_Entry.config(state="disabled")
        Mojito_Entry.config(state="disabled")
        Iced_cap_Entry.config(state="disabled")
        Doppio_Entry.config(state="disabled")
        Frappé_Entry.config(state="disabled")
        Cappucino_Entry.config(state="disabled")
        SexOn_Entry.config(state="disabled")
        Iced_latte_Entry.config(state="disabled")
        Espresso_Entry.config(state="disabled")

        var1.set(value=0)
        var2.set(value=0)
        var3.set(value=0)
        var4.set(value=0)
        var5.set(value=0)
        var6.set(value=0)
        var7.set(value=0)
        var8.set(value=0)
        var9.set(value=0)
        var10.set(value=0)
        var11.set(value=0)
        var12.set(value=0)
        var13.set(value=0)
        var14.set(value=0)
        var15.set(value=0)
        var16.set(value=0)
        var17.set(value=0)
        var18.set(value=0)

        listbox.delete(0, 20)
        listbox.insert("end", "=================================================")
        listbox.insert("end", "                                           RESTAURANT BILLING SYSTEM")
        listbox.insert("end", "=================================================")

    else:
        mb.showinfo("SYSTEM ALERT", "Canceled")


def total():
    l = int(Latte_Entry.get())
    e = int(Espresso_Entry.get())
    il = int(Iced_latte_Entry.get())
    v = int(SexOn_Entry.get())
    c = int(Cappucino_Entry.get())
    af = int(Frappé_Entry.get())
    am = int(Doppio_Entry.get())
    ic = int(Iced_cap_Entry.get())
    im = int(Mojito_Entry.get())
    sc = int(Cheese_Entry.get())
    su = int(Red_Entry.get())
    j = int(Pasta_Entry.get())
    w = int(lasagna_Entry.get())
    lc = int(Carnitas_Entry.get())
    k = int(Cheeseburger_Entry.get())
    ck = int(Layered_Entry.get())
    q = int(choc_Entry.get())
    p = int(Reuben_Entry.get())

    Latte, Espresso, Iced_latte, SexOn, Cappucino = 2, 1.69, 3, 2.30, 2
    Frappé, Doppio, Iced_cap, Mojito = 4, 3, 4, 1.50
    Cheese, Red, Pasta, lasagna, Carnitas = 2.95, 4, 9, 9.3, 6
    Cheeseburger, Layered, choc, Reuben = 3, 8, 6, 4.10

    tax, charge = 2.8, 1.0

    ll = Latte * l
    ee = Espresso * e
    ilil = Iced_latte * il
    vv = SexOn * v
    cc = Cappucino * c
    aaf = Frappé * af
    aam = Doppio * am
    icic = Iced_cap * ic
    imim = Mojito * im
    ssc = Cheese * sc
    ssu = Red * su
    jj = Pasta * j
    ww = lasagna * w
    llc = Carnitas * lc
    kk = Cheeseburger * k
    cck = Layered * ck
    qq = choc * q
    pp = Reuben * p

    drink = ll + ee + ilil + vv + cc + aaf + aam + icic + imim

    cake = ssc + ssu + jj + ww + llc + kk + cck + qq + pp

    if (drink + cake) == 0:
        tax = 0.0
        charge = 0.0

    sub = drink + cake + charge

    full_total = sub + tax

    listbox_Drinks.delete(0, 5)
    listbox_Cakes.delete(0, 5)
    listbox_Charge.delete(0, 5)
    Tax_Listbox.delete(0, 5)
    Sub_Listbox.delete(0, 5)
    Total_Listbox.delete(0, 5)

    listbox_Drinks.insert("end", "$ " + str('%.2f' % drink))
    listbox_Cakes.insert("end", "$ " + str('%.2f' % cake))
    listbox_Charge.insert("end", "$ " + str('%.2f' % charge))
    Tax_Listbox.insert("end", "$ " + str('%.2f' % tax))
    Sub_Listbox.insert("end", "$ " + str('%.2f' % sub))
    Total_Listbox.insert("end", "$ " + str('%.2f' % full_total))

    cash = int(Cash_Entry.get())
    remain = 0

    if cash != 0:
        remain = cash - full_total
        listbox_Remain.delete(0, 5)
        Entry_Cal.delete(0, 5)
        listbox_Remain.insert("end", "$ " + str('%.2f' % remain))

    return drink, cake, charge, tax, full_total, ll, ee, ilil, vv, cc, aaf, aam, icic, imim, ssc, ssu, jj, ww, llc, kk, cck, qq, pp, remain


def recipt():
    total_tuple = total()
    x = random.randint(1254, 3256)

    listbox.delete(0, 20)
    listbox.insert("end", "=================================================")
    listbox.insert("end", ("Ref : " + str(x) + "                          RESTAURANT BILLING SYSTEM"))
    listbox.insert("end", "=================================================")
    listbox.insert("end", "                                                 ")
    listbox.insert("end", "           Items                             Number of Items                              Total")
    listbox.insert("end", "                                                 ")
    if var1.get() == 1: listbox.insert("end", "     Latte                                                {}                                            {}".format(Latte_Entry.get(), total_tuple[5]))
    if var2.get() == 1: listbox.insert("end", "     Espresso                                          {}                                            {}".format(Espresso_Entry.get(), total_tuple[6]))
    if var3.get() == 1: listbox.insert("end", "     Iced Latte                                         {}                                            {}".format(Iced_latte_Entry.get(), total_tuple[7]))
    if var4.get() == 1: listbox.insert("end", "     Sex On The Beach                           {}                                            {}".format(SexOn_Entry.get(), total_tuple[8]))
    if var5.get() == 1: listbox.insert("end", "     Cappuccino                                     {}                                            {}".format(Cappucino_Entry.get(), total_tuple[9]))
    if var6.get() == 1: listbox.insert("end", "     Frappé                                             {}                                            {}".format(Frappé_Entry.get(), total_tuple[10]))
    if var7.get() == 1: listbox.insert("end", "     Doppio                                            {}                                            {}".format(Doppio_Entry.get(), total_tuple[11]))
    if var8.get() == 1: listbox.insert("end", "     Iced Cappuccino                             {}                                            {}".format(Iced_cap_Entry.get(), total_tuple[12]))
    if var9.get() == 1: listbox.insert("end", "     Mojito                                              {}                                            {}".format(Mojito_Entry.get(), total_tuple[13]))
    if var10.get() == 1: listbox.insert("end", "     Cheese Cake                                     {}                                           {}".format(Cheese_Entry.get(), total_tuple[14]))
    if var11.get() == 1: listbox.insert("end", "     Red Velvet Cake                                {}                                          {}".format(Red_Entry.get(), total_tuple[15]))
    if var12.get() == 1: listbox.insert("end", "     Pasta Puttanesca                              {}                                          {}".format(Pasta_Entry.get(), total_tuple[16]))
    if var13.get() == 1: listbox.insert("end", "     Lasagna Bolognese                          {}                                          {}".format(lasagna_Entry.get(), total_tuple[17]))
    if var14.get() == 1: listbox.insert("end", "     Carnitas Burrito                                {}                                          {}".format(Carnitas_Entry.get(), total_tuple[18]))
    if var15.get() == 1: listbox.insert("end", "     Cheeseburger                                   {}                                          {}".format(Cheeseburger_Entry.get(), total_tuple[19]))
    if var16.get() == 1: listbox.insert("end", "     Layered Rainbow Cake                     {}                                          {}".format(Layered_Entry.get(), total_tuple[20]))
    if var17.get() == 1: listbox.insert("end", "     Choc-Honeycomb Cake                    {}                                          {}".format(choc_Entry.get(), total_tuple[21]))
    if var18.get() == 1: listbox.insert("end", "     Reuben Sandwich                            {}                                          {}".format(Reuben_Entry.get(), total_tuple[22]))

    listbox.insert("end", "                                                 ")
    listbox.insert("end", "=================================================")
    listbox.insert("end", "                                                 ")
    listbox.insert("end", ("     Cost of Drinks : " + "                                                                            $ " + str('%.2f' % total_tuple[0])))
    listbox.insert("end", ("     Cost of Food Items : " + "                                                                    $ " + str('%.2f' % total_tuple[1])))
    listbox.insert("end", ("     Service Charge : " + "                                                                           $ " + str('%.2f' % total_tuple[2])))
    listbox.insert("end", ("     Paid Tax : " + "                                                                                      $ " + str('%.2f' % total_tuple[3])))
    listbox.insert("end", ("     Total : " + "                                                                                           $ " + str('%.2f' % total_tuple[4])))
    if float(Cash_Entry.get()) != 0: listbox.insert("end", "     Cash                                                                                               $ {}".format('%.2f' % float(Cash_Entry.get())))
    if float(Cash_Entry.get()) != 0: listbox.insert("end", "     Remain                                                                                           $ {}".format('%.2f' % float(total_tuple[23])))

    listbox.insert("end", "                                                 ")
    listbox.insert("end", "=================================================")


def exit_window():
    m = mb.askyesno("SYSTEM ALERT", "Are You Sure Exit From System \n")
    if m == 1:
        sys.exit()

    else:
        mb.showinfo("SYSTEM ALERT", "Canceled")


calculator = ""


def set_number7():
    global calculator
    calculator = calculator + "7"
    Entry_Cal.insert("end", "7")


def set_number8():
    global calculator
    calculator = calculator + "8"
    Entry_Cal.insert("end", "8")


def set_number9():
    global calculator
    calculator = calculator + "9"
    Entry_Cal.insert("end", "9")


def set_number6():
    global calculator
    calculator = calculator + "6"
    Entry_Cal.insert("end", "6")


def set_number5():
    global calculator
    calculator = calculator + "5"
    Entry_Cal.insert("end", "5")


def set_number4():
    global calculator
    calculator = calculator + "4"
    Entry_Cal.insert("end", "4")


def set_number3():
    global calculator
    calculator = calculator + "3"
    Entry_Cal.insert("end", "3")


def set_number2():
    global calculator
    calculator = calculator + "2"
    Entry_Cal.insert("end", "2")


def set_number1():
    global calculator
    calculator = calculator + "1"
    Entry_Cal.insert("end", "1")


def set_number0():
    global calculator
    calculator = calculator + "0"
    Entry_Cal.insert("end", "0")


def set_number_plus():
    global calculator
    calculator = calculator + " + "
    Entry_Cal.insert("end", " + ")


def set_number_minus():
    global calculator
    calculator = calculator + " - "
    Entry_Cal.insert("end", " - ")


def set_number_div():
    global calculator
    calculator = calculator + " / "
    Entry_Cal.insert("end", " / ")


def set_number_sub():
    global calculator
    calculator = calculator + " * "
    Entry_Cal.insert("end", " * ")


def set_number_dot():
    global calculator
    calculator = calculator + "."
    Entry_Cal.insert("end", ".")


def equal():
    Entry_Cal.delete(0, 50)
    global calculator
    Entry_Cal.insert("end", eval(calculator))


def clear():
    global calculator
    calculator = ""
    Entry_Cal.delete(0, 50)


def Latte():
    if var1.get() == 1:
        Latte_Entry.config(state="normal")
        Latte_Entry.delete(0, 5)
    else:
        Latte_Entry.delete(0, 5)
        Latte_Entry.insert("end", "0")
        Latte_Entry.config(state="disabled")


def Espresso():
    if var2.get() == 1:
        Espresso_Entry.config(state="normal")
        Espresso_Entry.delete(0, 5)
    else:
        Espresso_Entry.delete(0, 5)
        Espresso_Entry.insert("end", "0")
        Espresso_Entry.config(state="disabled")


def Iced_latte():
    if var3.get() == 1:
        Iced_latte_Entry.config(state="normal")
        Iced_latte_Entry.delete(0, 5)
    else:
        Iced_latte_Entry.delete(0, 5)
        Iced_latte_Entry.insert("end", "0")
        Iced_latte_Entry.config(state="disabled")


def SexOn():
    if var4.get() == 1:
        SexOn_Entry.config(state="normal")
        SexOn_Entry.delete(0, 5)
    else:
        SexOn_Entry.delete(0, 5)
        SexOn_Entry.insert("end", "0")
        SexOn_Entry.config(state="disabled")


def Cappucino():
    if var5.get() == 1:
        Cappucino_Entry.config(state="normal")
        Cappucino_Entry.delete(0, 5)
    else:
        Cappucino_Entry.delete(0, 5)
        Cappucino_Entry.insert("end", "0")
        Cappucino_Entry.config(state="disabled")


def Frappé():
    if var6.get() == 1:
        Frappé_Entry.config(state="normal")
        Frappé_Entry.delete(0, 5)
    else:
        Frappé_Entry.delete(0, 5)
        Frappé_Entry.insert("end", "0")
        Frappé_Entry.config(state="disabled")


def Doppio():
    if var7.get() == 1:
        Doppio_Entry.config(state="normal")
        Doppio_Entry.delete(0, 5)
    else:
        Doppio_Entry.delete(0, 5)
        Doppio_Entry.insert("end", "0")
        Doppio_Entry.config(state="disabled")


def Iced_cap():
    if var8.get() == 1:
        Iced_cap_Entry.config(state="normal")
        Iced_cap_Entry.delete(0, 5)
    else:
        Iced_cap_Entry.delete(0, 5)
        Iced_cap_Entry.insert("end", "0")
        Iced_cap_Entry.config(state="disabled")


def Mojito():
    if var9.get() == 1:
        Mojito_Entry.config(state="normal")
        Mojito_Entry.delete(0, 5)
    else:
        Mojito_Entry.delete(0, 5)
        Mojito_Entry.insert("end", "0")
        Mojito_Entry.config(state="disabled")


def Cheese():
    if var10.get() == 1:
        Cheese_Entry.config(state="normal")
        Cheese_Entry.delete(0, 5)
    else:
        Cheese_Entry.delete(0, 5)
        Cheese_Entry.insert("end", "0")
        Cheese_Entry.config(state="disabled")


def Red():
    if var11.get() == 1:
        Red_Entry.config(state="normal")
        Red_Entry.delete(0, 5)
    else:
        Red_Entry.delete(0, 5)
        Red_Entry.insert("end", "0")
        Red_Entry.config(state="disabled")


def Pasta():
    if var12.get() == 1:
        Pasta_Entry.config(state="normal")
        Pasta_Entry.delete(0, 5)
    else:
        Pasta_Entry.delete(0, 5)
        Pasta_Entry.insert("end", "0")
        Pasta_Entry.config(state="disabled")


def lasagna():
    if var13.get() == 1:
        lasagna_Entry.config(state="normal")
        lasagna_Entry.delete(0, 5)
    else:
        lasagna_Entry.delete(0, 5)
        lasagna_Entry.insert("end", "0")
        lasagna_Entry.config(state="disabled")


def Carnitas():
    if var14.get() == 1:
        Carnitas_Entry.config(state="normal")
        Carnitas_Entry.delete(0, 5)
    else:
        Carnitas_Entry.delete(0, 5)
        Carnitas_Entry.insert("end", "0")
        Carnitas_Entry.config(state="disabled")


def Cheeseburger():
    if var15.get() == 1:
        Cheeseburger_Entry.config(state="normal")
        Cheeseburger_Entry.delete(0, 5)
    else:
        Cheeseburger_Entry.delete(0, 5)
        Cheeseburger_Entry.insert("end", "0")
        Cheeseburger_Entry.config(state="disabled")


def Layered():
    if var16.get() == 1:
        Layered_Entry.config(state="normal")
        Layered_Entry.delete(0, 5)
    else:
        Layered_Entry.delete(0, 5)
        Layered_Entry.insert("end", "0")
        Layered_Entry.config(state="disabled")


def choc():
    if var17.get() == 1:
        choc_Entry.config(state="normal")
        choc_Entry.delete(0, 5)
    else:
        choc_Entry.delete(0, 5)
        choc_Entry.insert("end", "0")
        choc_Entry.config(state="disabled")


def Reuben():
    if var18.get() == 1:
        Reuben_Entry.config(state="normal")
        Reuben_Entry.delete(0, 5)
    else:
        Reuben_Entry.delete(0, 5)
        Reuben_Entry.insert("end", "0")
        Reuben_Entry.config(state="disabled")

window.geometry("1366x700+0+0")
window.title("Restaurant Billing System")

var1, var2, var3, var4 = tk.IntVar(),  tk.IntVar(),  tk.IntVar(),  tk.IntVar()
var5, var6, var7, var8, var9 = tk.IntVar(), tk.IntVar(),  tk.IntVar(),  tk.IntVar(),  tk.IntVar()
var10, var11, var12, var13, var14 = tk.IntVar(), tk.IntVar(),  tk.IntVar(),  tk.IntVar(),  tk.IntVar()
var15, var16, var17, var18 = tk.IntVar(),  tk.IntVar(),  tk.IntVar(),  tk.IntVar()
welcome = tk.Label(
    window,
    text="WELCOME",
    font=("Rockwell",40),
    # background="white"
)
welcome.place(relx=0.4,rely=0.07)
login_frame = tk.Frame(
    window,
    relief="flat",
    background="white"
)
login_frame.place(relx=0.25,rely=0.16,relwidth=0.5,relheight=0.5)
admin = tk.Button(
    login_frame,
    text="Manager login",
    font=("Rockwell",30),
    relief="flat",
    command=adminLogin
)
admin.place(relx=0.3,rely=0.1)
staff = tk.Button(
    login_frame,
    text="Staff login",
    font=("Rockwell",30),
    relief="flat",
    command=staffLogin
)
staff.place(relx=0.35,rely=0.4)
userName = tk.Label(
    login_frame,
    text="",
    font=("Rockwell",10),
    bg="white"
)

userName_entry = tk.Entry(
    login_frame
)

password = tk.Label(
    login_frame,
    text = "Password",
    font=("Rockwell",10),
    bg="white"
)

passwd_entry = tk.Entry(
    login_frame,
    show = "*",
)
back_button = tk.Button(
    login_frame,
    text="Back",
    font=("Rockwell",15),
    relief="flat",
    command=backbtn
)

login_button = tk.Button(
    login_frame,
    text="Login",
    font=("Rockwell",15),
    relief="flat",
    command=Login
)

Frame_Top = tk.Frame(
    window,
    background="#d9d9d8",
    borderwidth="8",
    relief='flat'
)
Frame_Top.place(relx=0, rely=0.003, relheight=1, relwidth=1)

Title = tk.Label(
    window,
    background="#000000",
    borderwidth="4",
    disabledforeground="#a3a3a3",
    font="-family {OCR A Std} -size 25 -weight bold",
    foreground="#ffffff",
    text='''RESTAURANT BILLING SYSTEM'''
)
Title.place(relx=0.004, rely=0.01, relheight=0.08, width=1353)

Frame_left = tk.Frame(Frame_Top,
    relief='flat',
    borderwidth="8",
    background="#d9d9d9"
)
Frame_left.place(relx=0, rely=0.08, relheight=0.645, relwidth=0.35)

Frame_middle = tk.Frame(Frame_Top,
    relief='flat',
    borderwidth="8",
    background="#d9d9d9"
)
Frame_middle.place(relx=0.347, rely=0.08, relheight=0.645, relwidth=0.354)

Frame_bottom = tk.Frame(Frame_Top,
    relief='flat',
    borderwidth="8",
    background="#c1c2c9"
)
Frame_bottom.place(relx=0, rely=0.72, relheight=0.28, relwidth=0.7)
Frame_right = tk.Frame(Frame_Top,
    relief='flat',
    borderwidth="8",
    background="#d9d9d9"
)
Frame_right.place(relx=0.697, rely=0.080, relheight=0.38, relwidth=0.31)

Frame_bottom_right = tk.Frame(Frame_Top,
    relief='flat',
    borderwidth="8",
    background="#d9d9d9"
)
Frame_bottom_right.place(relx=0.697, rely=0.43, relheight=0.5, relwidth=0.31)
#List of drinks
listbox_Drinks = tk.Listbox(Frame_bottom,
    background="#d9d9d8",
    disabledforeground="#a3a3a3",
    font="-family {Segoe UI} -size 14",
    foreground="black",
    highlightbackground="#d9d9d9",
    highlightcolor="black",
    borderwidth="5",
    justify="right"
)
listbox_Drinks.place(relx=0.3, rely=0.05, relheight=0.2, relwidth=0.2)
#List of Cakes
listbox_Cakes = tk.Listbox(Frame_bottom,
    background="#d9d9d8",
    disabledforeground="#a3a3a3",
    font="-family {Segoe UI} -size 14",
    foreground="black",
    highlightbackground="#d9d9d9",
    highlightcolor="black",
    borderwidth="5",
    justify="right"
)
listbox_Cakes.place(relx=0.3, rely=0.29, relheight=0.2, relwidth=0.2)
#List of Charge
listbox_Charge = tk.Listbox(Frame_bottom,
    background="#d9d9d8",
    disabledforeground="#a3a3a3",
    font="-family {Segoe UI} -size 14",
    foreground="black",
    highlightbackground="#d9d9d9",
    highlightcolor="black",
    borderwidth="5",
    justify="right"
)
listbox_Charge.place(relx=0.3, rely=0.54, relheight=0.2, relwidth=0.2)

Cash_Entry = tk.Entry(Frame_bottom,
    background="#d9d9d8",
    disabledforeground="#a3a3a3",
    font="-family {Segoe UI} -size 14",
    foreground="black",
    highlightbackground="#d9d9d9",
    highlightcolor="black",
    borderwidth="5",
    justify="right"
)
Cash_Entry.place(relx=0.3, rely=0.78, relheight=0.2, relwidth=0.2)

Tax_Listbox = tk.Listbox(Frame_bottom,
    background="#d9d9d8",
    disabledforeground="#a3a3a3",
    font="-family {Segoe UI} -size 14",
    foreground="black",
    highlightbackground="#d9d9d9",
    highlightcolor="black",
    borderwidth="5",
    justify="right"
)
Tax_Listbox.place(relx=0.75, rely=0.05, relheight=0.2, relwidth=0.2)

Sub_Listbox = tk.Listbox(Frame_bottom,
    background="#d9d9d8",
    disabledforeground="#a3a3a3",
    font="-family {Segoe UI} -size 14",
    foreground="black",
    highlightbackground="#d9d9d9",
    highlightcolor="black",
    borderwidth="5",
    justify="right"
)
Sub_Listbox.place(relx=0.75, rely=0.29, relheight=0.2, relwidth=0.2)

Total_Listbox = tk.Listbox(Frame_bottom,
    background="#d9d9d8",
    disabledforeground="#a3a3a3",
    font="-family {Segoe UI} -size 14",
    foreground="black",
    highlightbackground="#d9d9d9",
    highlightcolor="black",
    borderwidth="5",
    justify="right"
)
Total_Listbox.place(relx=0.75, rely=0.54, relheight=0.2, relwidth=0.2)

listbox_Remain = tk.Listbox(Frame_bottom,
    background="#d9d9d8",
    disabledforeground="#a3a3a3",
    font="-family {Segoe UI} -size 14",
    foreground="black",
    highlightbackground="#d9d9d9",
    highlightcolor="black",
    borderwidth="5",
    justify="right"
)
listbox_Remain.place(relx=0.75, rely=0.78, relheight=0.2, relwidth=0.2)
#THIS IS THE RECIEPT BOX
listbox = tk.Listbox(Frame_bottom_right,
    background="BLACK",
    disabledforeground="#a3a3a3",
    font="-family {Segoe UI} -size 8",
    foreground="White",
    highlightbackground="#d9d9d9",
    highlightcolor="black",
    borderwidth="5"
)
listbox.place(relx=0, rely=0, relheight=1, relwidth=1)
Entry_Cal = tk.Entry(Frame_right,
    background="#c1c2c9",
    disabledforeground="#a3a3a3",
    font="-family {Segoe UI} -size 14",
    foreground="black",
    insertbackground="black",
    borderwidth="5",
    justify="right"
)
Entry_Cal.place(relx=0.02, rely=0.03, height=45, relwidth=0.71, bordermode='ignore')
#LATTE ENTRY
Latte_Entry = tk.Entry(Frame_left,
    background="white",
    disabledforeground="#a3a3a3",
    font="-family {Segoe UI} -size 14",
    foreground="black",
    insertbackground="black",
    borderwidth="5"
)
Latte_Entry.place(relx=0.7, rely=0.1, height=35, relwidth=0.2, bordermode='ignore')
#ESPRESSO ENTRY
Espresso_Entry = tk.Entry(Frame_left,
    background="white",
    disabledforeground="#a3a3a3",
    font="-family {Segoe UI} -size 14",
    foreground="black",
    insertbackground="black",
    borderwidth="5"
)
Espresso_Entry.place(relx=0.7, rely=0.2, height=35, relwidth=0.2, bordermode='ignore')
#ICED LATTE
Iced_latte_Entry = tk.Entry(Frame_left,
    background="white",
    disabledforeground="#a3a3a3",
    font="-family {Segoe UI} -size 14",
    foreground="black",
    insertbackground="black",
    borderwidth="5"
)
Iced_latte_Entry.place(relx=0.7, rely=0.3, height=35, relwidth=0.2, bordermode='ignore')
#SEX ON THE BEACH ENTRY
SexOn_Entry = tk.Entry(Frame_left,
    background="white",
    disabledforeground="#a3a3a3",
    font="-family {Segoe UI} -size 14",
    foreground="black",
    insertbackground="black",
    borderwidth="5"
)
SexOn_Entry.place(relx=0.7, rely=0.4, height=35, relwidth=0.2, bordermode='ignore')
#CAPPUCINO ENTRY
Cappucino_Entry = tk.Entry(Frame_left,
    background="white",
    disabledforeground="#a3a3a3",
    font="-family {Segoe UI} -size 14",
    foreground="black",
    insertbackground="black",
    borderwidth="5"
)
Cappucino_Entry.place(relx=0.7, rely=0.5, height=35, relwidth=0.2, bordermode='ignore')
#FRAPPE ENTRY
Frappé_Entry = tk.Entry(Frame_left,
    background="white",
    disabledforeground="#a3a3a3",
    font="-family {Segoe UI} -size 14",
    foreground="black",
    insertbackground="black",
    borderwidth="5"
)
Frappé_Entry.place(relx=0.7, rely=0.6, height=35, relwidth=0.2, bordermode='ignore')
#DOPPIO ENTRY
Doppio_Entry = tk.Entry(Frame_left,
    background="white",
    disabledforeground="#a3a3a3",
    font="-family {Segoe UI} -size 14",
    foreground="black",
    insertbackground="black",
    borderwidth="5"
)
Doppio_Entry.place(relx=0.7, rely=0.7, height=35, relwidth=0.2, bordermode='ignore')
#ICED CAP
Iced_cap_Entry = tk.Entry(Frame_left,
    background="white",
    disabledforeground="#a3a3a3",
    font="-family {Segoe UI} -size 14",
    foreground="black",
    insertbackground="black",
    borderwidth="5"
)
Iced_cap_Entry.place(relx=0.7, rely=0.8, height=35, relwidth=0.2, bordermode='ignore')
#MOJITO ENTRY
Mojito_Entry = tk.Entry(Frame_left,
    background="white",
    disabledforeground="#a3a3a3",
    font="-family {Segoe UI} -size 14",
    foreground="black",
    insertbackground="black",
    borderwidth="5"
)
Mojito_Entry.place(relx=0.7, rely=0.9, height=35, relwidth=0.2, bordermode='ignore')
#CHEESE ENTRY
Cheese_Entry = tk.Entry(Frame_middle,
    background="white",
    disabledforeground="#a3a3a3",
    font="-family {Segoe UI} -size 14",
    foreground="black",
    insertbackground="black",
    borderwidth="5"
)
Cheese_Entry.place(relx=0.7, rely=0.1, height=35, relwidth=0.2, bordermode='ignore')
#RED ENTRY
Red_Entry = tk.Entry(Frame_middle,
    background="white",
    disabledforeground="#a3a3a3",
    font="-family {Segoe UI} -size 14",
    foreground="black",
    insertbackground="black",
    borderwidth="5"
)
Red_Entry.place(relx=0.7, rely=0.2, height=35, relwidth=0.2, bordermode='ignore')
#PASTA ENTRY
Pasta_Entry = tk.Entry(Frame_middle,
    background="white",
    disabledforeground="#a3a3a3",
    font="-family {Segoe UI} -size 14",
    foreground="black",
    insertbackground="black",
    borderwidth="5"
)
Pasta_Entry.place(relx=0.7, rely=0.3, height=35, relwidth=0.2, bordermode='ignore')
#LASAGNA ENTRY
lasagna_Entry = tk.Entry(Frame_middle,
    background="white",
    disabledforeground="#a3a3a3",
    font="-family {Segoe UI} -size 14",
    foreground="black",
    insertbackground="black",
    borderwidth="5"
)
lasagna_Entry.place(relx=0.7, rely=0.4, height=35, relwidth=0.2, bordermode='ignore')
#CARNITAS ENTRY
Carnitas_Entry = tk.Entry(Frame_middle,
    background="white",
    disabledforeground="#a3a3a3",
    font="-family {Segoe UI} -size 14",
    foreground="black",
    insertbackground="black",
    borderwidth="5"
)
Carnitas_Entry.place(relx=0.7, rely=0.5, height=35, relwidth=0.2, bordermode='ignore')
#CHEESEBURGER ENTRY
Cheeseburger_Entry = tk.Entry(Frame_middle,
    background="white",
    disabledforeground="#a3a3a3",
    font="-family {Segoe UI} -size 14",
    foreground="black",
    insertbackground="black",
    borderwidth="5"
)
Cheeseburger_Entry.place(relx=0.7, rely=0.6, height=35, relwidth=0.2, bordermode='ignore')
#LAYERED ENTRY
Layered_Entry = tk.Entry(Frame_middle,
    background="white",
    disabledforeground="#a3a3a3",
    font="-family {Segoe UI} -size 14",
    foreground="black",
    insertbackground="black",
    borderwidth="5"
)
Layered_Entry.place(relx=0.7, rely=0.7, height=35, relwidth=0.2, bordermode='ignore')
#CHOCOLATE ENTRY
choc_Entry = tk.Entry(Frame_middle,
    background="white",
    disabledforeground="#a3a3a3",
    font="-family {Segoe UI} -size 14",
    foreground="black",
    insertbackground="black",
    borderwidth="5"
)
choc_Entry.place(relx=0.7, rely=0.8, height=35, relwidth=0.2, bordermode='ignore')
#REUBEN INPUT
Reuben_Entry = tk.Entry(Frame_middle,
    background="white",
    disabledforeground="#a3a3a3",
    font="-family {Segoe UI} -size 14",
    foreground="black",
    insertbackground="black",
    borderwidth="5"
)
Reuben_Entry.place(relx=0.7, rely=0.9, height=35, relwidth=0.2, bordermode='ignore')
#CALCULATES THE TOTAL AMOUNT
TOTAL = tk.Button(
    relief="flat",
    activebackground="#ececec",
    activeforeground="#000000",
    background="#f2f2f2",
    borderwidth="5",
    disabledforeground="#a3a3a3",
    font="-family {Segoe UI} -size 14",
    foreground="#000000",
    highlightbackground="#d9d9d9",
    highlightcolor="black",
    pady="0",
    text='''TOTAL''',
    command=total
)
TOTAL.place(relx=0.699, rely=0.92, height=45, width=100)
#DISPLAYS THE RECEIPT
RECEIPT = tk.Button(
    relief="flat",
    activebackground="#ececec",
    activeforeground="#000000",
    background="#f2f2f2",
    borderwidth="5",
    disabledforeground="#a3a3a3",
    font="-family {Segoe UI} -size 14",
    foreground="#000000",
    highlightbackground="#d9d9d9",
    highlightcolor="black",
    pady="0",
    text='''RECEIPT''',
    command=recipt
)
RECEIPT.place(relx=0.773, rely=0.92, height=45, width=100)
#RESETS THE SYSTEM
RESET = tk.Button(
    relief="flat",
    activebackground="#ececec",
    activeforeground="#000000",
    background="#f2f2f2",
    borderwidth="5",
    disabledforeground="#a3a3a3",
    font="-family {Segoe UI} -size 14",
    foreground="#000000",
    highlightbackground="#d9d9d9",
    highlightcolor="black",
    pady="0",
    text='''RESET''',
    command=reset
)
RESET.place(relx=0.848, rely=0.92, height=45, width=100)

EXIT = tk.Button(
    relief="flat",
    activebackground="#ececec",
    activeforeground="#000000",
    background="#f2f2f2",
    borderwidth="5",
    disabledforeground="#a3a3a3",
    font="-family {Segoe UI} -size 14",
    foreground="#000000",
    highlightbackground="#d9d9d9",
    highlightcolor="black",
    pady="0",
    text='''EXIT''',
    command=exit_window
)
EXIT.place(relx=0.92, rely=0.92, height=45, width=100)

Button_7 = tk.Button(
    relief="flat",
    activebackground="#ececec",
    activeforeground="#000000",
    background="#f2f2f2",
    borderwidth="5",
    disabledforeground="#a3a3a3",
    font="-family {Segoe UI} -size 18",
    foreground="#000000",
    highlightbackground="#d9d9d9",
    highlightcolor="black",
    pady="0",
    text='''7''',
    command=set_number7
)
Button_7.place(relx=0.70, rely=0.17, height=45, width=100)

Button_8 = tk.Button(
    relief="flat",
    activebackground="#ececec",
    activeforeground="#000000",
    background="#f2f2f2",
    borderwidth="5",
    disabledforeground="#a3a3a3",
    font="-family {Segoe UI} -size 18",
    foreground="#000000",
    highlightbackground="#d9d9d9",
    highlightcolor="black",
    pady="0",
    text='''8''',
    command=set_number8
)
Button_8.place(relx=0.774, rely=0.17, height=45, width=100)

Button_9 = tk.Button(
    relief="flat",
    activebackground="#ececec",
    activeforeground="#000000",
    background="#f2f2f2",
    borderwidth="5",
    disabledforeground="#a3a3a3",
    font="-family {Segoe UI} -size 18",
    foreground="#000000",
    highlightbackground="#d9d9d9",
    highlightcolor="black",
    pady="0",
    text='''9''',
    command=set_number9
)
Button_9.place(relx=0.847, rely=0.17, height=45, width=100)

Button_plus = tk.Button(
    relief="flat",
    activebackground="#ececec",
    activeforeground="#000000",
    background="#f2f2f2",
    borderwidth="5",
    disabledforeground="#a3a3a3",
    font="-family {Segoe UI} -size 18",
    foreground="#000000",
    highlightbackground="#d9d9d9",
    highlightcolor="black",
    pady="0",
    text='''+''',
    command=set_number_plus
)
Button_plus.place(relx=0.92, rely=0.17, height=45, width=100)

Button_4 = tk.Button(
    relief="flat",
    activebackground="#ececec",
    activeforeground="#000000",
    background="#f2f2f2",
    borderwidth="5",
    disabledforeground="#a3a3a3",
    font="-family {Segoe UI} -size 18",
    foreground="#000000",
    highlightbackground="#d9d9d9",
    highlightcolor="black",
    pady="0",
    text='''4''',
    command=set_number4
)
Button_4.place(relx=0.70, rely=0.235, height=45, width=100)

Button_5 = tk.Button(
    relief="flat",
    activebackground="#ececec",
    activeforeground="#000000",
    background="#f2f2f2",
    borderwidth="5",
    disabledforeground="#a3a3a3",
    font="-family {Segoe UI} -size 18",
    foreground="#000000",
    highlightbackground="#d9d9d9",
    highlightcolor="black",
    pady="0",
    text='''5''',
    command=set_number5
)
Button_5.place(relx=0.774, rely=0.235, height=45, width=100)

Button_6 = tk.Button(
    relief="flat",
    activebackground="#ececec",
    activeforeground="#000000",
    background="#f2f2f2",
    borderwidth="5",
    disabledforeground="#a3a3a3",
    font="-family {Segoe UI} -size 18",
    foreground="#000000",
    highlightbackground="#d9d9d9",
    highlightcolor="black",
    pady="0",
    text='''6''',
    command=set_number6
)
Button_6.place(relx=0.847, rely=0.235, height=45, width=100)

Button_minus = tk.Button(
    relief="flat",
    activebackground="#ececec",
    activeforeground="#000000",
    background="#f2f2f2",
    borderwidth="5",
    disabledforeground="#a3a3a3",
    font="-family {Segoe UI} -size 18",
    foreground="#000000",
    highlightbackground="#d9d9d9",
    highlightcolor="black",
    pady="0",
    text='''-''',
    command=set_number_minus
)
Button_minus.place(relx=0.92, rely=0.235, height=45, width=100)

Button_1 = tk.Button(
    relief="flat",
    activebackground="#ececec",
    activeforeground="#000000",
    background="#f2f2f2",
    borderwidth="5",
    disabledforeground="#a3a3a3",
    font="-family {Segoe UI} -size 18",
    foreground="#000000",
    highlightbackground="#d9d9d9",
    highlightcolor="black",
    pady="0",
    text='''1''',
    command=set_number1
)
Button_1.place(relx=0.70, rely=0.3, height=45, width=100)

Button_2 = tk.Button(
    relief="flat",
    activebackground="#ececec",
    activeforeground="#000000",
    background="#f2f2f2",
    borderwidth="5",
    disabledforeground="#a3a3a3",
    font="-family {Segoe UI} -size 18",
    foreground="#000000",
    highlightbackground="#d9d9d9",
    highlightcolor="black",
    pady="0",
    text='''2''',
    command=set_number2
)
Button_2.place(relx=0.774, rely=0.3, height=45, width=100)

Button_3 = tk.Button(
    relief="flat",
    activebackground="#ececec",
    activeforeground="#000000",
    background="#f2f2f2",
    borderwidth="5",
    disabledforeground="#a3a3a3",
    font="-family {Segoe UI} -size 18",
    foreground="#000000",
    highlightbackground="#d9d9d9",
    highlightcolor="black",
    pady="0",
    text='''3''',
    command=set_number3
)
Button_3.place(relx=0.847, rely=0.3, height=45, width=100)

Button_multi = tk.Button(
    relief="flat",
    activebackground="#ececec",
    activeforeground="#000000",
    background="#f2f2f2",
    borderwidth="5",
    disabledforeground="#a3a3a3",
    font="-family {Segoe UI} -size 18",
    foreground="#000000",
    highlightbackground="#d9d9d9",
    highlightcolor="black",
    pady="0",
    text='''x''',
    command=set_number_sub
)
Button_multi.place(relx=0.92, rely=0.3, height=45, width=100)

Button_0 = tk.Button(
    relief="flat",
    activebackground="#ececec",
    activeforeground="#000000",
    background="#f2f2f2",
    borderwidth="5",
    disabledforeground="#a3a3a3",
    font="-family {Segoe UI} -size 18",
    foreground="#000000",
    highlightbackground="#d9d9d9",
    highlightcolor="black",
    pady="0",
    text='''0''',
    command=set_number0
)
Button_0.place(relx=0.70, rely=0.368, height=45, width=100)

Button_dot = tk.Button(
    relief="flat",
    activebackground="#ececec",
    activeforeground="#000000",
    background="#f2f2f2",
    borderwidth="5",
    disabledforeground="#a3a3a3",
    font="-family {Segoe UI} -size 18",
    foreground="#000000",
    highlightbackground="#d9d9d9",
    highlightcolor="black",
    pady="0",
    text='''.''',
    command=set_number_dot
)
Button_dot.place(relx=0.774, rely=0.368, height=45, width=100)

Button_equal = tk.Button(
    relief="flat",
    activebackground="#ececec",
    activeforeground="#000000",
    background="#f2f2f2",
    borderwidth="5",
    disabledforeground="#a3a3a3",
    font="-family {Segoe UI} -size 18",
    foreground="#000000",
    highlightbackground="#d9d9d9",
    highlightcolor="black",
    pady="0",
    text='''=''',
    command=equal
)
Button_equal.place(relx=0.847, rely=0.368, height=45, width=100)

Button_div = tk.Button(
    relief="flat",
    activebackground="#ececec",
    activeforeground="#000000",
    background="#f2f2f2",
    borderwidth="5",
    disabledforeground="#a3a3a3",
    font="-family {Segoe UI} -size 18",
    foreground="#000000",
    highlightbackground="#d9d9d9",
    highlightcolor="black",
    pady="0",
    text='''/''',
    command=set_number_div
)
Button_div.place(relx=0.92, rely=0.368, height=45, width=100)


Button_c = tk.Button(
    relief="flat",
    activebackground="#ececec",
    activeforeground="#000000",
    background="#f2f2f2",
    borderwidth="5",
    disabledforeground="#a3a3a3",
    font="-family {Segoe UI} -size 18",
    foreground="#000000",
    highlightbackground="#d9d9d9",
    highlightcolor="black",
    pady="0",
    text='''C''',
    command=clear
)
Button_c.place(relx=0.92, rely=0.105, height=45, width=100)


cost_of_drinks = tk.Label(Frame_bottom,
    background="#c1c2c9",
    disabledforeground="#a3a3a3",
    font="-family {aril black} -size 15",
    foreground="#000000",
    text='''Cost of Drinks'''
)
cost_of_drinks.place(relx=0.01, rely=0.1, height=25, width=200, bordermode='ignore')

cost_of_food = tk.Label(Frame_bottom,
    background="#c1c2c9",
    disabledforeground="#a3a3a3",
    font="-family {aril black} -size 15",
    foreground="#000000",
    text='''Cost of Food Items'''
)
cost_of_food.place(relx=0.01, rely=0.35, height=25, width=200, bordermode='ignore')

Service_Charge = tk.Label(Frame_bottom,
    background="#c1c2c9",
    disabledforeground="#a3a3a3",
    font="-family {aril black} -size 15",
    foreground="#000000",
    text='''Service charge'''
)
Service_Charge.place(relx=0.01, rely=0.6, height=25, width=200, bordermode='ignore')

Cash = tk.Label(Frame_bottom,
    background="#c1c2c9",
    disabledforeground="#a3a3a3",
    font="-family {aril black} -size 15",
    foreground="#000000",
    text='''Cash             '''
)
Cash.place(relx=0.01, rely=0.82, height=25, width=200, bordermode='ignore')

Paid_Tax = tk.Label(Frame_bottom,
    background="#c1c2c9",
    disabledforeground="#a3a3a3",
    font="-family {aril black} -size 15",
    foreground="#000000",
    text='''Paid Tax'''
)
Paid_Tax.place(relx=0.5, rely=0.1, height=25, width=200, bordermode='ignore')

Sub_Total = tk.Label(Frame_bottom,
    background="#c1c2c9",
    disabledforeground="#a3a3a3",
    font="-family {aril black} -size 15",
    foreground="#000000",
    text='''Sub Total'''
)
Sub_Total.place(relx=0.5, rely=0.35, height=25, width=200, bordermode='ignore')

Total_Cost = tk.Label(Frame_bottom,
    background="#c1c2c9",
    disabledforeground="#a3a3a3",
    font="-family {aril black} -size 15",
    foreground="#000000",
    text='''Total cost'''
)
Total_Cost.place(relx=0.5, rely=0.6, height=25, width=200, bordermode='ignore')

Remain = tk.Label(Frame_bottom,
    background="#c1c2c9",
    disabledforeground="#a3a3a3",
    font="-family {aril black} -size 15",
    foreground="#000000",
    text='''Remain'''
)
Remain.place(relx=0.5, rely=0.82, height=25, width=200, bordermode='ignore')


Label_Drinks = tk.Label(Frame_left,
    background="#d9d9d9",
    borderwidth="4",
    disabledforeground="#a3a3a3",
    font="-family {aril black} -size 17 -weight bold",
    foreground="black",
    text='''Drinks'''
)
Label_Drinks.place(relx=0.004, rely=0.0, relheight=0.08, width=130)


Label_Cakes = tk.Label(Frame_middle,
    background="#d9d9d9",
    borderwidth="4",
    disabledforeground="#a3a3a3",
    font="-family {aril black} -size 17 -weight bold",
    foreground="black",
    text='''Items'''
)
Label_Cakes.place(relx=0, rely=0.0, relheight=0.08, width=130)


Checkbutton_Latte = tk.Checkbutton(Frame_left,
    text="Latte",
    variable=var1,
    font="-family {Segoe UI} -size 14",
    background="#d9d9d9",
    command=Latte
)
Checkbutton_Latte.place(relx=0.1, rely=0.1, height=35, bordermode='ignore')

Espresso_Checkbutton = tk.Checkbutton(Frame_left,
    text="Espresso",
    variable=var2,
    font="-family {Segoe UI} -size 14",
    background="#d9d9d9",
    command=Espresso
)
Espresso_Checkbutton.place(relx=0.1, rely=0.2, height=35, bordermode='ignore')

Iced_latte_Checkbutton = tk.Checkbutton(Frame_left,
    text="Iced Latte",
    variable=var3,
    font="-family {Segoe UI} -size 14",
    background="#d9d9d9",
    command=Iced_latte
)
Iced_latte_Checkbutton.place(relx=0.1, rely=0.3, height=35, bordermode='ignore')


SexOn_Checkbutton = tk.Checkbutton(Frame_left,
    text="Sex On The Beach",
    variable=var4,
    font="-family {Segoe UI} -size 14",
    background="#d9d9d9",
    command=SexOn
)
SexOn_Checkbutton.place(relx=0.1, rely=0.4, height=35, bordermode='ignore')


Cappucino_Checkbutton = tk.Checkbutton(Frame_left,
    text="Cappuccino",
    variable=var5,
    font="-family {Segoe UI} -size 14",
    background="#d9d9d9",
    command=Cappucino
)
Cappucino_Checkbutton.place(relx=0.1, rely=0.5, height=35, bordermode='ignore')

Frappé_Checkbutton = tk.Checkbutton(Frame_left,
    text="Frappe",
    variable= var6,
    font="-family {Segoe UI} -size 14",
    background="#d9d9d9",
    command=Frappé
)
Frappé_Checkbutton.place(relx=0.1, rely=0.6, height=35, bordermode='ignore')


Doppio_Checkbutton = tk.Checkbutton(Frame_left,
    text="Doppio",
    variable= var7,
    font="-family {Segoe UI} -size 14",
    background="#d9d9d9",
    command=Doppio
)
Doppio_Checkbutton.place(relx=0.1, rely=0.7, height=35, bordermode='ignore')


Iced_cap_Checkbutton = tk.Checkbutton(Frame_left,
    text="Iced cappuccino",
    variable= var8,
    font="-family {Segoe UI} -size 14",
    background="#d9d9d9",
    command=Iced_cap
)
Iced_cap_Checkbutton.place(relx=0.1, rely=0.8, height=35, bordermode='ignore')

Mojito_Checkbutton = tk.Checkbutton(Frame_left,
    text="Mojito",
    variable= var9,
    font="-family {Segoe UI} -size 14",
    background="#d9d9d9",
    command=Mojito
)
Mojito_Checkbutton.place(relx=0.1, rely=0.9, height=35, bordermode='ignore')

Cheese_Checkbutton = tk.Checkbutton(Frame_middle,
    text="Cheese Cake",
    variable= var10,
    font="-family {Segoe UI} -size 14",
    background="#d9d9d9",
    command=Cheese
)
Cheese_Checkbutton.place(relx=0.1, rely=0.1, height=35, bordermode='ignore')

Red_Checkbutton = tk.Checkbutton(Frame_middle,
    text="Red Velvet Cake",
    variable= var11,
    font="-family {Segoe UI} -size 14",
    background="#d9d9d9",
    command=Red
)
Red_Checkbutton.place(relx=0.1, rely=0.2, height=35, bordermode='ignore')


Pasta_Checkbutton = tk.Checkbutton(Frame_middle,
    text="Pasta Puttanesca",
    variable= var12,
    font="-family {Segoe UI} -size 14",
    background="#d9d9d9",
    command=Pasta
)
Pasta_Checkbutton.place(relx=0.1, rely=0.3, height=35, bordermode='ignore')

lasagna_Checkbutton = tk.Checkbutton(Frame_middle,
    text="Lasagna Bolognese",
    variable= var13,
    font="-family {Segoe UI} -size 14",
    background="#d9d9d9",
    command=lasagna
)
lasagna_Checkbutton.place(relx=0.1, rely=0.4, height=35, bordermode='ignore')


Carnitas_Checkbutton = tk.Checkbutton(Frame_middle,
    text="Carnitas Burrito",
    variable= var14,
    font="-family {Segoe UI} -size 14",
    background="#d9d9d9",
    command=Frappé
)
Carnitas_Checkbutton.place(relx=0.1, rely=0.5, height=35, bordermode='ignore')

Cheeseburger_Checkbutton = tk.Checkbutton(Frame_middle,
    text="Cheeseburger",
    variable= var15,
    font="-family {Segoe UI} -size 14",
    background="#d9d9d9",
    command=Cheeseburger
)
Cheeseburger_Checkbutton.place(relx=0.1, rely=0.6, height=35, bordermode='ignore')

Layered_Checkbutton = tk.Checkbutton(Frame_middle,
    text="Layered Rainbow Cake",
    variable= var16,
    font="-family {Segoe UI} -size 14",
    background="#d9d9d9",
    command=Layered
)
Layered_Checkbutton.place(relx=0.1, rely=0.7, height=35, bordermode='ignore')

choc_Checkbutton = tk.Checkbutton(Frame_middle,
    text="Choc-Honeycomb Cake",
    variable= var17,
    font="-family {Segoe UI} -size 14",
    background="#d9d9d9",
    command=choc
)
choc_Checkbutton.place(relx=0.1, rely=0.8, height=35, bordermode='ignore')

Reuben_Checkbutton = tk.Checkbutton(Frame_middle,
    text="Reuben sandwich",
    variable= var18,
    font="-family {Segoe UI} -size 14",
    background="#d9d9d9",
    command=Reuben
)
Reuben_Checkbutton.place(relx=0.1, rely=0.9, height=35, bordermode='ignore')
if __name__ == '__main__':
    main()