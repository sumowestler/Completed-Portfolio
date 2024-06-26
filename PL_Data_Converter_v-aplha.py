# -*- coding: utf-8 -*-
"""
Created on Mon Jan  8 14:55:54 2024

@author: emartin
"""

# Imperting required modules
import pandas as pd
import os as op
import tkinter as tk
from tkinter import ttk

functionDataList = []


#universal Class for holding produnct data.

class functionData:
    def __init__(self, productType, wavelengthRange, machine):
        self.productType = productType
        self.wavelengthRange = wavelengthRange
        self.wavelength = []
        self.intensity = []
        self.intSignal = []
        self.FWHM = []
        self.machine = machine

## Populating the function data list (temporary)

## 15Epi0 PL#1 ##
Epi0DataOne = functionData("15Epi0", "1200 nm - 1300 nm", 1)
Epi0DataOne.wavelength.append([1.0642, -83.0084])
Epi0DataOne.intensity.append([0.4061, -0.0091])
Epi0DataOne.intSignal.append([0.3837, 0.1489])
Epi0DataOne.FWHM.append([0.9858, 0.2214])
functionDataList.append(Epi0DataOne)

ThirteenThirtyEMLDataThree = functionData("1330EML", "1300 nm - 1400 nm", 3)
ThirteenThirtyEMLDataThree.wavelength.append([1.0877, -118.4388])
ThirteenThirtyEMLDataThree.intensity.append([1.0877, -118.4388])
ThirteenThirtyEMLDataThree.FWHM.append([1.0877, -118.4388])
ThirteenThirtyEMLDataThree.intSignal.append([1.0877, -118.4388])
functionDataList.append(ThirteenThirtyEMLDataThree)
        
# print(productTypeDataBase["productType"]["wavelengthRange"])

## class for injecting new fucntions:
    
#class for taking user input.

class userQuery:
    data = functionDataList
    osConnection =  "S:\Test Equip\PL#3\PL#3 Data"
    osConnection2 = "S:\Test Equip\PL#1\PL#1 Data"
    def __init__(self, i):
        self.i = i
        self.productType = None
        self.wavelengthRange = None
        self.queryList = []
        self.wavelength =None
        self.intensity = None
        self.intSignal = None
        self.FWHM = None
        self.wavelengthSTDList = []
        self.intensitySTDList = []
        self.intSignalSTDList = []
        self.FWHMSTDList = []
        self.AVG_Peak_Lambda_List = []
        self.AVG_Peak_Int_List = []
        self.AVG_Int_Signal_list = []
        self.AVG_FWHM_List = []
        self.AVG_Laser_Power = []
        self.AVG_Laser_Power_cleaned = []
        self.yWavelengh = []
        self.yIntensity = []
        self.yIntSignal = []
        self.yFWHM = []
        self.slopeWavelength = None
        self.interceptWavelength = None
        self.slopeIntSignal = None
        self.interceptIntSignal = None
        self.slopeInt = None
        self.interceptInt = None
        self.slopeFWHM = None
        self.interceptFWHM = None
        self.dataName = []
        self.outputMessage = ""
        self.committMessage = None
        self.initial_pick = []
        self.machine = None
    
    def set_productType1330EML(self):
        self.productType = "1330EML"
        print("yes")
        
    def set_productRange1300to1400(self):
        self.wavelengthRange = "1300 nm - 1400 nm"
        print("yes")
    
    def set_productType15Epi0(self):
        self.productType = ("15Epi0")
        print("yes")
    
    def set_pproductRange1200to1300(self):
        self.wavelengthRange = "1200 nm - 1300 nm"
        print("yes")
        
    def get_productType(self):
        return self.productType
    
    def set_productType(self, x):
        self.productType = x
        print("ok")
    
    def get_wavelengthRange(self):
        return self.wavelengthRange
    
    def set_wavelengthRange(self, x):
        self.wavelengthRange = x
        print("ok")
    
    def get_queryList(self):
        return self.queryList
    
    def set_queryList(self, x):
        self.queryList = x
        
    def get_intensity(self):
        return self.intensity
    
    def set_intensity(self, x):
        self.intensity = x
    
    def get_intSignal(self):
        return self.intSignal
    
    def set_intSignal(self, x):
        self.intSignal = x
    
    def get_FWHM(self):
        return self.FWHM
    
    def set_FWHM(self, x):
        self.FWHM = x
    
    def get_wavelength(self):
        return self.wavelength
    
    def set_wavelength(self, x):
        self.wavelength = x
    
    def get_machine(self):
        return self.machine
    
    def set_machine(self, x):
        self.machine = x
    # def query(self):
    #     lst = []
    #     a = input("Please choose your product type?") # will accept a list of values.
    #     b = input("Please choose your product wavelength") # will accept a list of values.
    #     n = int(input("Please enter number of items to convert"))
        
    #     for i in range(0, n):
    #         ele = input("Please enter file name")
    #         lst.append(ele)
    #     self.queryList = lst
    #     self.productType = a
    #     self.wavelengthRange = b    
    # update query insrtance with apropriate function data
    def query_update(self):
        for function in functionDataList:
            if function.productType == self.productType and function.wavelengthRange == self.wavelengthRange and function.machine == self.machine:
                self.set_wavelength(function.wavelength)
                self.set_intensity(function.intensity)
                self.set_intSignal(function.intSignal)
                self.set_FWHM(function.FWHM)
    #Populate conversionjmaker instance
                self.slopeWavelength = self.wavelength[0][0]
                self.interceptWavelength = self.wavelength[0][1]
                self.slopeInt = self.intensity[0][0]
                self.interceptInt = self.intensity[0][1]
                self.slopeIntSignal = self.intSignal[0][0]
                self.interceptIntSignal = self.intSignal[0][1]
                self.slopeFWHM = self.FWHM[0][0]
                self.interceptFWHM = self.FWHM[0][1]
                for item in self.initial_pick:
                    self.queryList.append(item)
                print("ok")
                self.committMessage = "You have selected the product: {} with wavelength range: {} on machine: {}. To proceed, press the 'Begin Conversion' button.".format(self.productType, self.wavelengthRange, self.machine)
                # self.outputMessage = "You have selected the product {} in the wavelength range {} on PL # {}".format(self.productType, self.wavelengthRange, self.machine)
                #Breakpoint for debugging
                # print(self.queryList)
                # print(self.slopeInt)
        
    def data_Reader(self) -> list:
        if self.machine == 3:
            for item in self.queryList:
                data = pd.read_csv(r'{}\{}'.format(self.osConnection, item), encoding='unicode_escape', sep=" :", engine='python')
                data2 = data.reset_index()
                wavelengthData = float(data2["Nanometrics RPM PL Wafer Mapping System - version 9.17.0"].iloc[39][6:12])
                intensityData = float(data2["Nanometrics RPM PL Wafer Mapping System - version 9.17.0"].iloc[39][18:25])
                intSignalData = float(data2["Nanometrics RPM PL Wafer Mapping System - version 9.17.0"].iloc[39][32:38])
                fwhmData = float(data2["Nanometrics RPM PL Wafer Mapping System - version 9.17.0"].iloc[39][48:54])
                wavelengthDataSTD = float(data2["Nanometrics RPM PL Wafer Mapping System - version 9.17.0"].iloc[40][6:12])
                intensityDataSTD = float(data2["Nanometrics RPM PL Wafer Mapping System - version 9.17.0"].iloc[40][18:25])
                intSignalDataSTD = float(data2["Nanometrics RPM PL Wafer Mapping System - version 9.17.0"].iloc[40][32:38])
                fwhmDataSTD = float(data2["Nanometrics RPM PL Wafer Mapping System - version 9.17.0"].iloc[40][48:54])
                self.AVG_Peak_Lambda_List.append(wavelengthData)
                self.AVG_Peak_Int_List.append(intensityData)
                self.AVG_Int_Signal_list.append(intSignalData)
                self.AVG_FWHM_List.append(fwhmData)
                self.dataName.append(item)
                self.wavelengthSTDList.append(wavelengthDataSTD)
                self.intensitySTDList.append(intensityDataSTD)
                self.intSignalSTDList.append(intSignalDataSTD)
                self.FWHMSTDList.append(fwhmDataSTD)
                m = self.slopeWavelength
                b = self.interceptWavelength
                y = (m*wavelengthData) + b
                ry = round(y, 1)
                self.yWavelengh.append(ry)
            
                m = self.slopeInt
                b = self.interceptInt
                y = (m*intensityData) + b
                ry = round(y, 3)
                self.yIntensity.append(ry)
            
                m = self.slopeIntSignal
                b = self.interceptIntSignal
                y = (m*intSignalData) + b
                ry = round(y, 1)
                self.yIntSignal.append(ry)
        
                m = self.slopeFWHM
                b = self.interceptFWHM
                y = (m*fwhmData) + b
                ry = round(y, 1)
                self.yFWHM.append(ry)
                
                self.outputMessage = "Filename: {}, Wavelength(nm): {}, Wavelength STDEV(nm): {}, Intensity(V): {}, Intensity STDEV(V): {}, IntSignal(A.U.): {}, IntSignal STDEV(A.U.): {},  FWHM(nm): {}, FWHM STDEV(nm) {}".format(self.dataName, self.yWavelengh, self.wavelengthSTDList, self.yIntensity, self.intensitySTDList,  self.yIntSignal, self.intSignalSTDList, self.yFWHM, self.FWHMSTDList)
                print("ok")
        elif self.machine == 1:
            for item in self.queryList:
                data = pd.read_csv(r'{}\{}'.format(self.osConnection2, item), encoding='unicode_escape', sep=" :", engine='python')
                data2 = data.reset_index()
                wavelengthData = float(data2["Nanometrics RPM PL Wafer Mapping System - version 7.65"].iloc[40][6:12])
                intensityData = float(data2["Nanometrics RPM PL Wafer Mapping System - version 7.65"].iloc[40][18:25])
                intSignalData = float(data2["Nanometrics RPM PL Wafer Mapping System - version 7.65"].iloc[40][32:38])
                fwhmData = float(data2["Nanometrics RPM PL Wafer Mapping System - version 7.65"].iloc[40][48:54])
                wavelengthDataSTD = float(data2["Nanometrics RPM PL Wafer Mapping System - version 7.65"].iloc[41][6:12])
                intensityDataSTD = float(data2["Nanometrics RPM PL Wafer Mapping System - version 7.65"].iloc[41][18:25])
                intSignalDataSTD = float(data2["Nanometrics RPM PL Wafer Mapping System - version 7.65"].iloc[41][32:38])
                fwhmDataSTD = float(data2["Nanometrics RPM PL Wafer Mapping System - version 7.65"].iloc[41][48:54])
                self.AVG_Peak_Lambda_List.append(wavelengthData)
                self.AVG_Peak_Int_List.append(intensityData)
                self.AVG_Int_Signal_list.append(intSignalData)
                self.AVG_FWHM_List.append(fwhmData)
                self.dataName.append(item)
                self.wavelengthSTDList.append(wavelengthDataSTD)
                self.intensitySTDList.append(intensityDataSTD)
                self.intSignalSTDList.append(intSignalDataSTD)
                self.FWHMSTDList.append(fwhmDataSTD)
        # for item in self.osConnection:
        #     if item in self.queryList:
        #         data = pd.read_csv(r"S:\Test Equip\PL#3\PL#3 Data\{}".format(item), error_bad_lines=False,keep_default_na=False, sep=":", names=["Field", "Value", "Misc"])
        #         data_bottom = pd.read_csv(r"S:\Test Equip\PL#3\PL#3 Data\{}".format(item), header=None, error_bad_lines=False, skiprows=28, keep_default_na=False,
        #                                   names=["x (nm)", "Y (nm)", "Peak Lambda (nm)", "Peak Int (Volt)", "Int. Signal (A.U)", "FWHM (nm)", "6"])
        #         data_bottom["Laser (nm)"] = data["Value"].iloc[13]
        #         data_bottom["Laser Power (mW)"] = data["Value"].iloc[14]
        #         self.AVG_Peak_Lambda_List.append(st.mean(data_bottom["Peak Lambda (nm)"]))
        #         self.AVG_Peak_Int_List.append(st.mean(data_bottom["Peak Int (Volt)"]))
        #         self.AVG_Int_Signal_list.append(st.mean(data_bottom["Int. Signal (A.U)"]))
        #         self.AVG_FWHM_List.append(st.mean(data_bottom["FWHM (nm)"]))
        #         self.AVG_Laser_Power.append(data_bottom["Laser Power (mW)"].iloc[0])
## make a method for runnig the items in the list through appropriate linear functions
                m = self.slopeWavelength
                b = self.interceptWavelength
                y = (m*wavelengthData) + b
                ry = round(y, 1)
                self.yWavelengh.append(ry)
            
                m = self.slopeInt
                b = self.interceptInt
                y = (m*intensityData) + b
                ry = round(y, 3)
                self.yIntensity.append(ry)
            
                m = self.slopeIntSignal
                b = self.interceptIntSignal
                y = (m*intSignalData) + b
                ry = round(y, 1)
                self.yIntSignal.append(ry)
        
                m = self.slopeFWHM
                b = self.interceptFWHM
                y = (m*fwhmData) + b
                ry = round(y, 1)
                self.yFWHM.append(ry)
                
                self.outputMessage = "Filename: {}, Wavelength(nm): {}, Wavelength STDEV(nm): {}, Intensity(V): {}, Intensity STDEV(V): {}, IntSignal(A.U.): {}, IntSignal STDEV(A.U.): {},  FWHM(nm): {}, FWHM STDEV(nm) {}".format(self.dataName, self.yWavelengh, self.wavelengthSTDList, self.yIntensity, self.intensitySTDList,  self.yIntSignal, self.intSignalSTDList, self.yFWHM, self.FWHMSTDList)
        
        # print(self.yWavelengh)
        # print(self.yIntensity)
        # print(self.yIntSignal)
        # print(self.yFWHM)
        # print(self.outputMessage)
        
        
        def excel_conversion(self):
            pass



## making the converter program


#First block

# i = 0 # starting instance counter



# Query = userQuery(i)
# #populating object
# a = Query.query()
# b = dataMaker(i)
# b.queryList = Query.queryList
# b.data_Reader()

# data = pd.read_csv('28-2801-3in-1577EML-1@11MW-5_spm.dat', error_bad_lines=False,keep_default_na=False, sep=":", names=["Field", "Value", "Misc"])
# data_bottom = pd.read_csv(r"S:\Test Equip\PL#3\PL#3 Data\{}".format('28-2801-3in-1577EML-1@11MW-5_spm.dat'), header=None, error_bad_lines=False, skiprows=28, keep_default_na=False, names=["x (nm)", "Y (nm)", "Peak Lambda (nm)", "Peak Int (Volt)", "Int. Signal (A.U)", "FWHM (nm)", "6"])


## Front End objects

## Conversion Screen
# window_Converter = tk.Tk()
# window_Converter.title("Converter")
# window_width = 800
# window_height = 900
# screen_width = window_Converter.winfo_screenwidth()
# screen_height = window_Converter.winfo_screenheight()
# center_x = int(screen_width/2 - window_width / 2)
# center_y = int(screen_height/2 - window_height / 2)
# window_Converter.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')

    
# ## Main frame for program
# window = tk.Tk()
# window.title("PL3 Converter")
# window_width = 300
# window_height = 200
# screen_width = window.winfo_screenwidth()
# screen_height = window.winfo_screenheight()
# center_x = int(screen_width/2 - window_width / 2)
# center_y = int(screen_height/2 - window_height / 2)
# window.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')

# #Function to open new window.

# def create()
# buttonConverter = ttk.Button(master=window, text="Convert Data", command= lambda: window_Converter.mainloop() )
# buttonExit = ttk.Button(master = window, text="Exit", command=lambda: window.quit())
# buttonExit.pack()
# buttonConverter.pack()

# window.mainloop()
# window_Converter.lift(window)

## Second set of top_level objects

class Window(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)

        self.geometry('300x100')
        self.title('Toplevel Window')

        ttk.Button(self,
                text='Close',
                command=self.destroy).pack(expand=False, side='bottom')

class App(tk.Tk):
    def __init__(self):
        super().__init__()

        self.geometry('300x200')
        self.title('Main Window')

        # place a button on the root window
        ttk.Button(self,
                text='Convert Data',
                command=self.open_conversion).pack(expand=True)

    def open_window(self, i):
        window = i
        window.grab_set()

    def open_conversion(self):
        conversionQuery = userQuery(1)
        # test query list
        windowCon = Window(self)
        windowCon.geometry("900x900")
        windowCon.title("Data Converter")
        queryFrame = ttk.LabelFrame(windowCon,text= 'User Query', height=200, width=200)
        queryFrame['padding'] = 5
        queryFrame['borderwidth'] = 5
        queryFrame['relief'] = 'groove'
        queryFrame.pack(side= "top", expand=True, fill='both')
        windowCon.grab_set()
        # Excel Conversion Frame
        excel_convert_frame = ttk.Labelframe(windowCon, text= "Export Data", height=200, width=200)
        excel_convert_frame['padding'] = 5
        excel_convert_frame['borderwidth'] = 5
        excel_convert_frame['relief'] = 'groove'
        excel_convert_frame.pack(side='bottom', expand=True, fill='both')
        # Output Frames
        resultFrame = ttk.Labelframe(windowCon, text="Query Results", height=200, width=200)
        resultFrame['padding'] = 5
        resultFrame['borderwidth'] = 5
        resultFrame['relief'] = 'groove'
        resultFrame.pack(side = 'bottom', expand=True, fill= 'both')
        # menu for picking product type
        machineNumberMenuButton = ttk.Menubutton(queryFrame, text="Select PL Machine Number")
        menu3 = tk.Menu(machineNumberMenuButton, tearoff=False)
        productTypeMenuButton = ttk.Menubutton(queryFrame, text="Select a product type")
        menu = tk.Menu(productTypeMenuButton, tearoff=False)
        menu.add_command(label = "1330EML", command = conversionQuery.set_productType1330EML)
        menu.add_command(label = "15Epi0", command = conversionQuery.set_productType15Epi0)
        productWavelengthRangeMenuButton = ttk.Menubutton(queryFrame, text="Select a product range")
        menu2 = tk.Menu(productWavelengthRangeMenuButton, tearoff=False)
        menu2.add_command(label = "1300 nm - 1400 nm", command = conversionQuery.set_productRange1300to1400)
        menu2.add_command(label = "1200 nm - 1300 nm", command = conversionQuery.set_pproductRange1200to1300)
        machineNumberMenuButton["menu"] = menu3
        productWavelengthRangeMenuButton["menu"] = menu2
        productTypeMenuButton["menu"] = menu
        productTypeMenuButton.pack(side='top')
        productWavelengthRangeMenuButton.pack(side = 'top')
        machineNumberMenuButton.pack(side = 'top')
        # Button to begin conversion process
        ttk.Button(queryFrame, text = "Begin Conversion", command=conversionQuery.data_Reader).pack(expand=False, side='bottom') # fill command later.
        # Button to commit changes to query and maker classes 
        ttk.Button(queryFrame, text="Commit", command=conversionQuery.query_update).pack(expand=False, side='bottom')
        # List box for browsing data for query
        browser = op.listdir("S:\Test Equip\PL#3\PL#3 Data")
        browserDAT = [x for x in browser if ".txt" in x]
        browsing = tk.Variable(value=browserDAT)
        browser2 = op.listdir('S:\Test Equip\PL#1\PL#1 Data')
        browserDAT2 = [x for x in browser2 if ".txt" in x]
        browsing2 = tk.Variable(value=browserDAT2)
        listboxQuery = tk.Listbox(queryFrame, listvariable= browsing, height=10, selectmode=tk.SINGLE)
        listboxQuery.pack(expand=True, fill=tk.BOTH, side = tk.LEFT)
        #function to switch between machines
        def switch_3():
            conversionQuery.set_machine(3)
            if conversionQuery.machine == 1:
                pass
            elif conversionQuery.machine == 3:
                listboxQuery.delete(0, tk.END)
                print("ok")
                for item in browserDAT:
                    listboxQuery.insert(tk.END, item)
        def switch_1():
            conversionQuery.set_machine(1)
            if conversionQuery.machine == 3:
                pass
            elif conversionQuery.machine == 1:
                listboxQuery.delete(0, tk.END)
                print("ok")
                for item in browserDAT2:
                    listboxQuery.insert(tk.END, item)
        menu3.add_command(label = "1", command = switch_1)
        menu3.add_command(label = "3", command = switch_3)
        # Function to switch between  1 and 3Z
        # Listbox for query tracking
        selectedQueryBox = tk.Listbox(queryFrame, height=10, selectmode=tk.SINGLE)
        selectedQueryBox.pack(expand=True, fill=tk.BOTH, side = tk.LEFT) # change list variable to take clicks from listBoxQuery
        # Text Box for dsiplaying Converssion Parameters
        # Add callback function for selection
        
        def on_select(event):
            # Get selected item
            index = event.widget.curselection()[0]
            value = event.widget.get(index)
            # insert into another listbox
            selectedQueryBox.insert(tk.END, value)
            conversionQuery.initial_pick.append(value)
            
        #bind selected querybox
        listboxQuery.bind("<<ListboxSelect>>", on_select)
        # scrollbar for list box
        queryScrollbar = tk.Scrollbar(listboxQuery)
        queryScrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        listboxQuery.config(yscrollcommand=queryScrollbar.set)
        queryScrollbar.config(command=listboxQuery.yview) #insert Searchbar for practical reasons
        selectedQueryBoxScrollBar = tk.Scrollbar(selectedQueryBox)
        selectedQueryBoxScrollBar.pack(side=tk.RIGHT, fill=tk.Y)
        selectedQueryBox.config(yscrollcommand=selectedQueryBoxScrollBar.set)
        selectedQueryBoxScrollBar.config(command=selectedQueryBox.yview)
        #Output widgets.
        # variable connection to result lists.
        output = tk.Text(resultFrame, height=100, width=100)
        output.insert(tk.END, conversionQuery.outputMessage)
        output.pack(expand=True)
        def update():
            a = conversionQuery.outputMessage
            b = conversionQuery.committMessage
            if a == "" and b == None:
                output.insert(tk.END, a)
                output.after(1000, update)
            elif a == "" and b != None:
                output.insert(tk.END, b)
                conversionQuery.committMessage = ""
                output.after(1000, update)
            else:
                output.delete('1.0', tk.END)
                output.insert(tk.END, a)
        output.after(1000, update)
        # output.insert(tk.END, conversionQuery.outputMessage)
        # Search Bar for finding queries faster.
        search_var = tk.StringVar()
        modify =tk.Entry(queryFrame, textvariable=search_var)
        modify.pack(side=tk.LEFT, fill=tk.BOTH)
        modify.focus_set()
        #Search settings for variables and callback function for find button.
        def find():
            if conversionQuery.machine == 3:
                while search_var =="":
                    pass
                findList = []
                for item in browserDAT:
                    if search_var.get() in item:
                        findList.append(item)
                listboxQuery.delete(0, tk.END)
                for item in findList:
                    listboxQuery.insert(tk.END, item)
            elif conversionQuery.machine == 1:
                while search_var =="":
                    pass
                findList = []
                for item in browserDAT2:
                    if search_var.get() in item:
                        findList.append(item)
                listboxQuery.delete(0, tk.END)
                for item in findList:
                    listboxQuery.insert(tk.END, item)
            
            
        find_button = tk.Button(queryFrame, text="Find", command=find)
        find_button.pack(side=tk.LEFT)
        
        # def highlight_searched(*args):
        #     search = search_var
        #Conversion to Excel Button
        pathtext = tk.StringVar()
        pathtext.set("Enter Run #/Wafer ID")
        pathdir = ttk.Label(excel_convert_frame, textvariable=pathtext) # does not work
        pathdir.pack(side='top')
        direct = tk.StringVar(None)
        direntry = ttk.Entry(excel_convert_frame, textvariable=direct, width=50)
        direntry.pack(side='left')
        
        #Defining a callback function for the conversion button
        
        def export_excel():
            if conversionQuery.machine == 3:
                filepath_converted_data = "S:\Test Equip\PL#3\convertedData"
                data_to_export = pd.DataFrame()
                nameSeries  = pd.Series(conversionQuery.dataName)
                data_to_export["File Name"] = nameSeries
                wavelengthSeries = pd.Series(conversionQuery.yWavelengh)
                data_to_export["Adjusted Peak Lambda (nm)"] = wavelengthSeries
                wavelengthSeriesSTD = pd.Series(conversionQuery.wavelengthSTDList)
                data_to_export["Adjusted Peak Lambda STDEV (nm)"] = wavelengthSeriesSTD
                intensitySeries = pd.Series(conversionQuery.yIntensity)
                data_to_export["Adjusted Peak Intensity (Volt)"] = intensitySeries
                intensitySeriesSTD = pd.Series(conversionQuery.intensitySTDList)
                data_to_export["Adjusted Peak Intensity STDEV (Volt)"] = intensitySeriesSTD
                intSignalSeries = pd.Series(conversionQuery.yIntSignal)
                data_to_export["Adjusted Int Signal (A.U.)"] = intSignalSeries
                intSignalSeriesSTD = pd.Series(conversionQuery.intSignalSTDList)
                data_to_export["Adjusted Int Signal STDEV (A.U.)"] = intSignalSeriesSTD
                FWHMSeries = pd.Series(conversionQuery.yFWHM)
                data_to_export["Adjusted FWHM (nm)"] = FWHMSeries
                FWHMSeriesSTD = pd.Series(conversionQuery.FWHMSTDList)
                data_to_export["Adjusted FWHM STDEV (nm)"] = FWHMSeriesSTD
                data_to_export.to_excel("{}\{}.xlsx".format(filepath_converted_data, direct.get()))
            elif conversionQuery.machine == 1:
                filepath_converted_data = "S:\Test Equip\PL#1\convertedData"
                data_to_export = pd.DataFrame()
                nameSeries  = pd.Series(conversionQuery.dataName)
                data_to_export["File Name"] = nameSeries
                wavelengthSeries = pd.Series(conversionQuery.yWavelengh)
                data_to_export["Adjusted Peak Lambda (nm)"] = wavelengthSeries
                wavelengthSeriesSTD = pd.Series(conversionQuery.wavelengthSTDList)
                data_to_export["Adjusted Peak Lambda STDEV (nm)"] = wavelengthSeriesSTD
                intensitySeries = pd.Series(conversionQuery.yIntensity)
                data_to_export["Adjusted Peak Intensity (Volt)"] = intensitySeries
                intensitySeriesSTD = pd.Series(conversionQuery.intensitySTDList)
                data_to_export["Adjusted Peak Intensity STDEV (Volt)"] = intensitySeriesSTD
                intSignalSeries = pd.Series(conversionQuery.yIntSignal)
                data_to_export["Adjusted Int Signal (A.U.)"] = intSignalSeries
                intSignalSeriesSTD = pd.Series(conversionQuery.intSignalSTDList)
                data_to_export["Adjusted Int Signal STDEV (A.U.)"] = intSignalSeriesSTD
                FWHMSeries = pd.Series(conversionQuery.yFWHM)
                data_to_export["Adjusted FWHM (nm)"] = FWHMSeries
                FWHMSeriesSTD = pd.Series(conversionQuery.FWHMSTDList)
                data_to_export["Adjusted FWHM STDEV (nm)"] = FWHMSeriesSTD
                data_to_export.to_excel("{}\{}.xlsx".format(filepath_converted_data, direct.get()))
        
        convert_to_excel = tk.Button(excel_convert_frame , text= "Convert to Excel", command=export_excel)
        convert_to_excel.pack(expand=False, side='bottom')
        

        
root = App()
root.title("Pl#3 Converter")



if __name__ == "__main__":
   root.mainloop()

