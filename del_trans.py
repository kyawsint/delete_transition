#!/usr/bin/python3

from Tkinter import *
import psycopg2
import tkMessageBox

class Checkbar(Frame):
    def __init__(self, parent=None, picks=[], side=LEFT, anchor=W):
        Frame.__init__(self, parent)
        self.vars = []
        for pick in picks:
            var = IntVar()
            chk = Checkbutton(self, text=pick, variable=var)
            chk.pack(side=side, anchor=anchor, expand=YES)
            self.vars.append(var)
    def state(self):
        return map((lambda var: var.get()), self.vars)
if __name__ == '__main__':
    root = Tk()
    var = StringVar()
    lbl_title = Label( root, textvariable=var, relief=RAISED )
    var.set("Delete Transitions")
    lbl_title.pack(side=TOP)
    lbl_title.config(width=20, font=14)
    lbl_dbname = Label(root, text="Database Name")
    lbl_dbname.pack(side = TOP)
    txt_dbname = Entry(root, bd =5)
    txt_dbname.pack(side= TOP)

    lng = Checkbar(root, ['Account Advanced Line', 'Account Advanced', 'Account Move Line', 'Account Move'])
    lng1 = Checkbar(root, ['Account Invoice', 'Account Voucher', 'Account Bank Statement', 'Account Cost Line'])
    lng2 = Checkbar(root, ['General Payment Line', 'General Payment', 'General Received Line', 'General Received'])
    lng3 = Checkbar(root, ['Account Asset Asset', 'Purchase Order', 'Stock Picking', 'Stock Move'])
    lng4 = Checkbar(root, ['Sale Order', 'Purchase Requisition', 'Account Period', 'Account Fiscalyear'])
    lng5 = Checkbar(root, ['POS Order', 'POS Session'])

    lng.pack(side=TOP, fill=X)
    lng1.pack(side=TOP, fill=X)
    lng2.pack(side=TOP, fill=X)
    lng3.pack(side=TOP, fill=X)
    lng4.pack(side=TOP, fill=X)
    lng5.pack(side=TOP, fill=X)
    lng.config(relief=GROOVE, bd=3)
    lng1.config(relief=GROOVE, bd=3)
    lng2.config(relief=GROOVE, bd=3)
    lng3.config(relief=GROOVE, bd=3)
    lng4.config(relief=GROOVE, bd=3)
    lng5.config(relief=GROOVE, bd=3)

    def del_trans():
        all_lng=list(lng.state())+list(lng1.state())+list(lng2.state())+list(lng3.state())+list(lng4.state())
        tables=['account_advanced_line', 'account_advanced', 'account_move_line', 'account_move',
        'account_invoice', 'account_voucher', 'account_bank_statement', 'account_cost_line',
        'general_payment_line', 'general_payment', 'general_received_line', 'general_received',
        'account_asset_asset', 'purchase_order', 'stock_picking', 'stock_move',
        'sale_order', 'purchase_requisition', 'account_period', 'account_fiscalyear','pos_order','pos_session']

        if txt_dbname.get()=='':
            tkMessageBox.showerror(title="Error !!!",message="Please enter database name !!!")
        else:
            db_name=txt_dbname.get()
            conn = psycopg2.connect(database=db_name,host='localhost',port='5432')
            cr = conn.cursor()

            for i in range(0,len(tables)):
                if all_lng[i]==1:
                    cr.execute("delete from "+tables[i]+" ")
                    cr.execute("commit")
                elif all_lng[i]==0:
                    continue
    Button(root, text='Quit', command=root.quit).pack(side=RIGHT)
    Button(root, text='OK', command=del_trans).pack(side=RIGHT)
    root.mainloop()

