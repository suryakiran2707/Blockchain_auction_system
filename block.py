from tkinter import messagebox, ttk
from main import createBlock
from tkinter import *
from verify import ver
import datetime
import nltk

root = Tk(className="Tender System")


class block:
    def __init__(self):
        self.blockChain = [createBlock("0", "0", str(datetime.datetime.now()), "0", "")]
        self.Transactionpool = []
        self.tenders = []
        self.tenderQuotes = []
        self.amount=[]

    def verifyTransaction(self, a, b, c, privatekey):
        a = int(a)
        b = int(b)
        c = int(c)
        fr=[a,b,c]
        fr.sort()
        [a,b,c]=fr
        if (ver.veriprivate(privatekey)):
            self.mineBlock(
                self.Transactionpool[a - 1][2] + " is the tender winner, Bid value = "+str(self.amount[a-1])+" for contract " + self.Transactionpool[a - 1][0][
                    0] + " by " + self.Transactionpool[a - 1][0][1] + ". " + self.Transactionpool[b - 1][
                    2] + " is the tender winner , Bid value = "+str(self.amount[b-1]) +" for contract "+ self.Transactionpool[b - 1][0][0] + " by " +
                self.Transactionpool[b - 1][0][1] + ". " + self.Transactionpool[c - 1][
                    2] + " is the tender winner, Bid value = "+str(self.amount[c-1]) +" for contract " + self.Transactionpool[c - 1][0][0] + " by " +
                self.Transactionpool[c - 1][0][1]+".",
                ver.getname(privatekey))
            del self.Transactionpool[c - 1]
            del self.Transactionpool[b - 1]
            del self.Transactionpool[a - 1]
            del self.amount[c - 1]
            del self.amount[b - 1]
            del self.amount[a - 1]
            alert("Sucsess", "Block mined sucessfully")

        else:
            alert("error", "Private key not valid")
        self.printall()
        inifunc()

    def mineBlock(self, data, name):
        for k in range(0, 10000000000000000):
            if (createBlock(self.blockChain[-1].hash, data, str(datetime.datetime.now()), k, name).calhash()[
                0:4] == "0000"):
                print(createBlock(self.blockChain[-1].hash, data, str(datetime.datetime.now()), k, name));
                self.blockChain.append(
                    createBlock(self.blockChain[-1].hash, data, str(datetime.datetime.now()), k, name))
                break;
        print("Block sucessfully mined")

    def addTransaction(self, data):
        self.Transactionpool.append(data)


    def tenderThis(self, index, privatekey, amount):
        index = int(index)
        amount = int(amount)
        if index <= 0 or index > len(self.tenders):
            return

        if(amount<0):
            alert("error", "amount cannot be less than 0")
            return

        if ver.getprivate(privatekey).get("public_key")==self.tenders[index-1][1]:
            alert("error","You cannot tender for your contract")


        if ver.veriprivate(privatekey) == False:
            alert("error", "wrong private key")
            return

        while (index - len(self.tenderQuotes) > 0):
            self.tenderQuotes.append([]);
        apo = ver.getprivate(privatekey).get("public_key")
        self.tenderQuotes[index - 1].append([amount, apo])

        self.printall()
        inifunc()

    def addTender(self, name, privatekey):
        if not ver.veriprivate(privatekey):
            alert("ERROR", "wrong private key")
            return

        self.tenders.append([name, ver.getprivate(privatekey).get("public_key")])
        inifunc()

    def endit(self, index, privatekey):
        index = int(index)
        if not ver.veriprivate(privatekey):
            alert("Error", "wrong private key")
            return
        print(str(self.tenders[index - 1]))
        if (str(self.tenders[index - 1][1]) != str(ver.getprivate(privatekey).get("public_key"))):
            alert("Error", "You are not the owner for this")

        if index > len(self.tenderQuotes) or len(self.tenderQuotes[index - 1]) == 0:
            alert("Error","No one has bided till now you can cancel it only atleast one user tenders for your contract")
            return
        mini = 1000000
        minicontrator = ""
        for x in self.tenderQuotes[index - 1]:
            if (x[0] < mini):
                mini = x[0]
                minicontrator = x[1]
        transactiondiff = []
        for x in self.tenderQuotes[index - 1]:
            transactiondiff.append([x[0] - mini, x[1]])
        self.Transactionpool.append([self.tenders[index - 1], transactiondiff, minicontrator])
        self.tenders.pop(index - 1)
        self.tenderQuotes.pop(index - 1)
        self.amount.append(mini);
        inifunc()

    def printall(self):
        for x in self.tenderQuotes:
            print(str(x) + "\n")
        for x in self.tenders:
            print(str(x) + "\n")
        for x in self.Transactionpool:
            print(str(x) + "\n")
        for x in self.blockChain:
            print(x)

    def set(self):
        i = 1
        if (len(self.tenders) == 0):
            wind = Label(root, text="NO CURRENT TENDERS", font=('Times 14', 15), borderwidth=20, pady=10)
            wind.pack()

            return
        for x in self.tenders:
            frame = LabelFrame(root, bg='#FFC0CB', padx=10)
            name.append(
                Label(frame, text="Contract : " + x[0], font=('Times 14', 15), borderwidth=20, pady=10, bg='#FFC0CB'))
            contractor.append(Label(frame, text="Posted by : " + x[1], font=('Times 14', 15), bg='#FFC0CB'))
            name[i - 1].grid(row=0, column=0, padx=10, pady=10)
            contractor[i - 1].grid(row=0, column=1, padx=10, pady=10)
            keyentry.append(Entry(frame, width=25))
            pkey=Label(frame, text="Enter you private key :", font=('Times 14', 15), bg='#FFC0CB')
            pkey.grid(row=0,column=2,padx=5)
            keyentry[i - 1].grid(row=0, column=3, padx=10, pady=5)
            pkey = Label(frame, text="Enter the tender amount :", font=('Times 14', 15), bg='#FFC0CB')
            pkey.grid(row=0, column=4, padx=5)
            amount.append(Entry(frame, width=25))
            amount[i - 1].grid(row=0, column=5, padx=5, pady=5)
            button.append(Button(frame, text="Tender This", font=('Times 14', 15), padx=5,
                                 command=lambda i=i: self.tenderThis(int(i), keyentry[int(i) - 1].get(),
                                                                     amount[int(i) - 1].get())))
            button[i - 1].grid(row=0, column=6,padx=5)
            button1.append(Button(frame, text="End This", font=('Times 14', 15), padx=5,
                                  command=lambda i=i: self.endit(int(i), keyentry[int(i) - 1].get())))
            button1[i - 1].grid(row=0, column=7,padx=5)
            frame.pack()
            i = i + 1

    def settpool(self):
        i = 1
        if (len(self.Transactionpool) == 0):
            wind = Label(root, text="NO TRANSACTIONS TO MINE", font=('Times 14', 15), borderwidth=20, pady=10)
            wind.pack()
            return
        for x in self.Transactionpool:
            frame = LabelFrame(root, bg='#FFC0CB', padx=30)
            # frame.grid_propagate(0)
            name = Label(frame, text=str(i) + ". " + "Name : " + x[0][0], font=('Times 14', 15), borderwidth=20,
                         pady=10, bg='#FFC0CB')
            name.grid(row=0, column=0)
            key = Label(frame, text="Posted by : " + x[0][1], font=('Times 14', 15), borderwidth=20, pady=10,
                        bg='#FFC0CB')
            key.grid(row=0, column=1)
            diff = Label(frame, text="Transaction difference amounts are : " + str(x[1]), font=('Times 14', 15),
                         borderwidth=20, pady=10,
                         bg='#FFC0CB')
            diff.grid(row=0, column=2, columnspan=2)
            key = Label(frame, text="Minimum tender by : " + x[2], font=('Times 14', 15), borderwidth=20, pady=10,
                        bg='#FFC0CB')
            key.grid(row=0, column=4)
            frame.pack()
            i = i + 1
        frame = LabelFrame(root, bg='#FFC0CB', padx=30)
        key = Label(frame, text="Enter first transaction number : ", font=('Times 14', 15), borderwidth=20, pady=10,
                    bg='#FFC0CB')
        key.grid(row=0, column=0)
        val = Entry(frame, width=25, font=('Times 14', 15))
        val.grid(row=0, column=1)
        key = Label(frame, text="Enter second transaction number : ", font=('Times 14', 15), borderwidth=20, pady=10,
                    bg='#FFC0CB')
        key.grid(row=0, column=2)
        val1 = Entry(frame, width=25, font=('Times 14', 15))
        val1.grid(row=0, column=3)
        key = Label(frame, text="Enter third transaction number : ", font=('Times 14', 15), borderwidth=20, pady=10,
                    bg='#FFC0CB')
        key.grid(row=1, column=0)
        val2 = Entry(frame, width=25, font=('Times 14', 15))
        val2.grid(row=1, column=1)
        key = Label(frame, text="Enter private key : ", font=('Times 14', 15), borderwidth=20, pady=10,
                    bg='#FFC0CB')
        key.grid(row=1, column=2)
        val3 = Entry(frame, width=25, font=('Times 14', 15))
        val3.grid(row=1, column=3)
        submit = Button(frame, text="Start mining",
                        command=lambda: obj.verifyTransaction(val.get(), val1.get(), val2.get(), val3.get()), padx=10,
                        pady=10,
                        font=('Times 14', 10), borderwidth=5)
        submit.grid(row=4, column=2, columnspan=2)
        frame.pack()

    def settrans(self):
        if (len(self.blockChain) == 1):
            wind = Label(root, text="NO BLOCKS TO SHOW", font=('Times 14', 15), borderwidth=20, pady=10)
            wind.pack()
            return
        t = 1
        for i in range(1, len(self.blockChain)):
            x = self.blockChain[i]
            if (x.hash != createBlock(x.prevblockhash, x.data, x.timestamp, x.nonce, x.name).calhash()):
                alert("error", "Data integrity is lost")
            transactions = nltk.sent_tokenize(x.data)
            for y in transactions:
                wind = Label(root, text=str(t) + ". " + y, font=('Times 14', 15), borderwidth=20, pady=10)
                wind.pack()
                t = t + 1

    def viewDetails(self, user):
        global root
        root.destroy()
        root = Tk(className="Tender System - Add new Tender")
        w, h = root.winfo_screenwidth(), root.winfo_screenheight()
        root.geometry("%dx%d+0+0" % (w, h))
        m = Label(root, text="Tender System", width=100, bg="#ADD8E6", font=('Times 14', 20), height=4)
        m.pack()

        for i in range(1, len(self.blockChain)):
            x = self.blockChain[i]
            if (x.hash != createBlock(x.prevblockhash, x.data, x.timestamp, x.nonce, x.name).calhash()):
                alert("error", "Data integrity is lost")
            transactions = nltk.sent_tokenize(x.data)
            t = 1
            for y in transactions:
                print(y[-2:])
                if user == y[0:2] or user == y[-3:-1]:
                    wind = Label(root, text=str(t) + ". " + y, font=('Times 14', 15), borderwidth=20, pady=10)
                    wind.pack()
                    t = t + 1
        back = Button(text="Back", font=('Times 14', 10), borderwidth=5, command=inifunc, padx=10, pady=10)
        back.pack()


def inifunc():
    global root
    root.destroy()
    root = Tk(className="Tender System - Bid for tender")
    w, h = root.winfo_screenwidth(), root.winfo_screenheight()
    root.geometry("%dx%d+0+0" % (w, h))
    global name
    name = []
    global contractor
    contractor = []
    global keyentry
    keyentry = []
    global amount
    amount = []
    global button
    button = []
    global button1
    button1 = []
    m = Label(root, text="Tender System", width=100, bg="#ADD8E6", font=('Times 14', 20), height=4)
    m.pack()
    labelframe = ttk.LabelFrame(root)
    labelframe.pack();
    back = Button(labelframe,text="ADD NEW TENDER", font=('Times 14', 10), borderwidth=5, command=addwind, padx=10, pady=10)
    back.grid(row=0,column=0,padx=30)
    back = Button(labelframe,text="MINE BLOCK", font=('Times 14', 10), borderwidth=5, command=mine, padx=10, pady=10)
    back.grid(row=0,column=1,padx=30)
    back = Button(labelframe,text="CHECK AND PRINT ALL BLOCKS", font=('Times 14', 10), borderwidth=5, command=printblocks, padx=10,
                  pady=10)
    back.grid(row=0,column=2,padx=30)
    labelframe1 = ttk.LabelFrame(labelframe)
    labelframe1.grid(row=0,column=3)
    name4 = Label(labelframe1, text="Enter public key you want to search", font=('Times 14', 15), padx=5, pady=5)
    name4.grid(row=0, column=0)
    nametext = Entry(labelframe1, font=('Times 14', 15))
    nametext.grid(row=0, column=1, padx=2, pady=2)
    back = Button(labelframe1, text="SEARCH", font=('Times 14', 10), borderwidth=5,
                  command=lambda: obj.viewDetails(nametext.get()), padx=10,
                  pady=10)
    back.grid(row=0, column=2)
    obj.set()


def addwind():
    global root
    root.destroy()
    root = Tk(className="Tender System - Add new Tender")
    w, h = root.winfo_screenwidth(), root.winfo_screenheight()
    root.geometry("%dx%d+0+0" % (w, h))
    labelframe = ttk.LabelFrame(root)

    # provide padding
    labelframe.pack(padx=30, pady=30)
    name = Label(labelframe, text="Enter contract name", font=('Times 14', 20), padx=50, pady=50)
    name.grid(row=0, column=0)
    nametext = Entry(labelframe, font=('Times 14', 20))
    nametext.grid(row=0, column=1, padx=10, pady=10)

    name1 = Label(labelframe, text="Enter private key", font=('Times 14', 20), padx=50, pady=50)
    name1.grid(row=1, column=0)
    nametext1 = Entry(labelframe, font=('Times 14', 20))
    nametext1.grid(row=1, column=1, padx=10, pady=10)
    submit = Button(text="Add", command=lambda: obj.addTender(nametext.get(), nametext1.get()), padx=10, pady=10,
                    font=('Times 14', 10), borderwidth=5)
    submit.pack()
    back = Button(text="Back", font=('Times 14', 10), borderwidth=5, command=inifunc, padx=10, pady=10)
    back.pack()


def mine():
    global root
    root.destroy()
    root = Tk(className="Tender System - Add new Tender")
    w, h = root.winfo_screenwidth(), root.winfo_screenheight()

    root.geometry("%dx%d+0+0" % (w, h))
    m = Label(root, text="Tender System", width=100, bg="#ADD8E6", font=('Times 14', 20), height=4)
    m.pack()
    obj.settpool()
    back = Button(text="Back", font=('Times 14', 10), borderwidth=5, command=inifunc, padx=10, pady=10)
    back.pack()


def printblocks():
    global root
    root.destroy()
    root = Tk(className="Tender System - Add new Tender")
    w, h = root.winfo_screenwidth(), root.winfo_screenheight()
    root.geometry("%dx%d+0+0" % (w, h))
    m = Label(root, text="Tender System", width=100, bg="#ADD8E6", font=('Times 14', 20), height=4)
    m.pack()
    obj.settrans()
    back = Button(text="Back", font=('Times 14', 10), borderwidth=5, command=inifunc, padx=10, pady=10)
    back.pack()


def alert(title, message, kind='info'):
    if kind not in ('error', 'warning', 'info'):
        raise ValueError('Unsupported alert kind.')

    show_method = getattr(messagebox, 'show{}'.format(kind))
    show_method(title, message)


name = []
contractor = []
keyentry = []
amount = []
button = []
button1 = []
obj = block()
scrollbar = Scrollbar(root)
scrollbar.pack(side=RIGHT, fill=Y)
# addwind()
inifunc()
root.mainloop()
