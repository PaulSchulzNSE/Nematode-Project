#things that need to be finished for rough draft project
"""
- First you need to add the citations into popup window 4 (completed)
- second you need to also add in citations and a conclusion into popup window 5 (completed)
- thrid you need to put an image as the background of the homepage, and place all the buttons in the center (completed)
- fourthly, make all the popup windows large enough to display all needed information, maybe consider a scrolling window aswell (completed)
- finally, you need to make all buttons the same size, and upload this project to github so you can have a link to the website 
- side note, do not forget to copy all of the text used into a word doc to create the transcript of this website, it is also part of this draft.(completed)

"""
#End of things that need to be finished for the rough draft project

#importing the needed ui libraries to serve as the front end of the code
import tkinter as tk
from tkinter import ttk
from tkinter import *
from tkinter import messagebox 

#importing the image library
from PIL import Image, ImageTk
#creating the main window for the application
root = tk.Tk()
root.geometry("2395x1200")
root.configure(bg = "violet")
root.title("Nematode Homepage")

#this section of code creates a grid with three columns which is used to center buttons and place images to the sides of buttons
root.grid_columnconfigure(0, weight = 1)
root.grid_columnconfigure(1, weight = 0)
root.grid_columnconfigure(2, weight = 1)


# Homepage image
home_image = Image.open("Slug_Image.jpeg")

# Resize image
home_image = home_image.resize((600, 400))

# Convert for Tkinter
home_photo = ImageTk.PhotoImage(home_image)

# Display image
home_image_label = tk.Label(root, image=home_photo)
home_image_label.image = home_photo

home_image_label.grid(row=0, column=0, pady=5)

#inserting another image onto the homepage to make it look more stylish
home_image_2 = Image.open("Homepage_image_2.jpeg")

#resizing the second image
home_image_2 = home_image_2.resize((600, 400))

#converting the new image for tkinter
home_photo_2 = ImageTk.PhotoImage(home_image_2)

#displaying the second image
home_image_2_label = tk.Label(root, image = home_photo_2)
home_image_2_label.image = home_photo_2

#placing the image on the home window grid
home_image_2_label.grid(row = 0, column = 2, pady =5)

#end of inserting images on homepage

#information window 1
#this button and function that runs this button, contains a breif description of nematodes and why they are important
def show_info_button_1():

    info_window = tk.Toplevel(root)

    info_window.title("What are Nematodes?")
    info_window.geometry("2395x1200")

    #adding information to the popup window
    title = tk.Label(
        info_window,
        text = "Nematode Information",
        font = ("Arial", 16, "bold")
    )
    title.pack(pady=10)

    #inserting the image
    # Open image file
    image = Image.open("Nematode_1.jpeg")

    # Resize image (width, height)
    image = image.resize((400, 300))

    # Convert image for Tkinter
    photo = ImageTk.PhotoImage(image)

    # Create label to display image
    image_label = tk.Label(info_window, image=photo)

    # Keep a reference to prevent image disappearing
    image_label.image = photo

    # Add image to window
    image_label.pack(pady=10)

    #end of inserting in the image

    info_text = """
    Nematodes are microscopic worms found in nearly every environment on earth, The focus of nematodes in this experiment however will be those found inside slugs.   

    Nematodes play important roles in soil ecology, nutrient cycling, agriculture, and scientific research   

    """

    info_label = tk.Label(
        info_window,
        text = info_text,
        justify = "left",
        wraplength = 450
    )

    info_label.pack(padx = 20,pady = 10 )

#here is the code for the actual button that you click on, the above is the function telling the button what to do
button_1 = tk.Button(
    root, 
    text = "What are nematodes?",
    font = ("Arial", 16),
    bg = "green",
    command = show_info_button_1,
    width = 30
)

button_1.grid(row = 1, column = 1, padx = 10, pady = 5)

#end of code for information window 1

#start of code for information window 2

#function for information window 2
def show_info_button_2():

    info_window = tk.Toplevel(root)

    info_window.title("Question, Hypothesis and Prediction")
    info_window.geometry("2395x1200")

    #adding information to the popup window
    title = tk.Label(
        info_window,
        text = "Question, Hypothesis and Prediction",
        font = ("Arial", 16, "bold")
    )
    title.pack(pady=10)

    #inserting the image
    # Open image file
    image = Image.open("Question_Mark.jpeg")

    # Resize image (width, height)
    image = image.resize((400, 300))

    # Convert image for Tkinter
    photo = ImageTk.PhotoImage(image)

    # Create label to display image
    image_label = tk.Label(info_window, image=photo)

    # Keep a reference to prevent image disappearing
    image_label.image = photo

    # Add image to window
    image_label.pack(pady=10)

    #end of inserting in the image

    info_text = """
    The main question this experiement strives to answer is what factors determine the richnes of nematodes? Now as many know slugs are generally found in wet climates, so natrually this experimental question evolves into: what effect does water have on nemeatode richness in slugs?
    This evolved form of the question is what my scientific group is aiming to answer as understanding how water, the main factor in slug climate, effects nematodes can help scientists across the globe create a better and safer nematode based pest control for slugs because the world will have a better understanding of how nematodes function in the slugs perfered climate.

    My groups Hypothesis was: 

    If a slug is found near running water, it will have more nematodes as they spread more near running water.

    Our prediction was: 

    If the hypothesis is true then more nematode species will be found in a slug collected near running water compared to a slug collected further from running water.
    """

    info_label = tk.Label(
        info_window,
        text = info_text,
        justify = "left",
        wraplength = 450
    )

    info_label.pack(padx = 20, pady = 10)


#This is the code for the actual button object
button_2 = tk.Button(
    root, 
    text = "Question, Hypothesis, and Prediction",
    font = ("Arial", 16),
    bg = "green",
    command = show_info_button_2,
    width = 30
)

button_2.grid(row = 2, column = 1, padx = 10, pady = 5)

#End of code for information window 2



#Start of code for information window 3

#function for information window 3
def show_info_button_3():

    info_window = tk.Toplevel(root)

    info_window.title("Experimental Design")
    info_window.geometry("2395x1200")

    #adding information to the popup window
    title = tk.Label(
        info_window,
        text = "Experimental Design",
        font = ("Arial", 16, "bold")
    )
    title.pack(pady=10)

    #inserting the image
    # Open image file
    image = Image.open("Experiment_Cartoon.jpeg")

    # Resize image (width, height)
    image = image.resize((400, 300))

    # Convert image for Tkinter
    photo = ImageTk.PhotoImage(image)

    # Create label to display image
    image_label = tk.Label(info_window, image=photo)

    # Keep a reference to prevent image disappearing
    image_label.image = photo

    # Add image to window
    image_label.pack(pady=10)

    #end of inserting in the image

    info_text = """
    What Question is Being tested?
        - What effect does water have on nematode richness in slugs?  

    Independent Variables of Experiment: 
        - This refers to the variables being changed by myself and my fellow scientists in the experiment  
        - We will be changing the distance we collect a slug from the water source and the type of slug collected, for this we will only be collecting banana slugs. 

    Dependent Variables of Experiment: 
        - This refers to the variables that reflect collected data such as nematode amount or richness  
        - The dependent variables of this experiment will be, nematode abundance (specifically abundance of the nematodes capable of killing the slugs)  

    Treatments and Conditions of Experiment: 
        - This refers directly to individual trials of each experiment  
        - For this experiment we will do 20 trials at equal distance increments 
        - The first trial will begin at a slug collection distance of 5 meters and increase to a maximum distance of 105 meters from the running water source (trial 1 = 5 meters, trial 20 = 105 meters)  
        - our control group for this experiment will be a collection distance of 0 meters from the water, of which we expect to have the most nematodes of all the samples collected 

    Replication and Analysis of Experiment:  
        - This refers to how many trials we will conduct and how we as a team plan to analyze our data  
        - It has already been mentioned in the treatments and conditions section, however, to be clear this experiment will have 20 total trials starting at 5 meters and ending at 105 meters from the running water source   
        - For the analysis of the data, we as a group intend to use Excel spreadsheets to collect our data and create a graph of our data. Then using our graphed data determine a relationship between the dependent and independent variable via a linear trend 

    General Setup:  
        - This refers specifically to where we will be keeping the slugs for study and the conditions they will be in  
        - our team has developed a small enclosure for each of our slugs to reside in, it contains a moist environment and an equal amount of food for each slug, this ensures no harm will come to the slugs  
        - After the experiment is over, we intend to return each slug to where we found them as when we pick up a slug in the field, we will mark the location and slug 
    """

    info_label = tk.Label(
        info_window,
        text = info_text,
        justify = "left",
        wraplength = 450
    )

    info_label.pack(padx = 20,pady = 10 )


#code for actual button for information window 3
button_3 = tk.Button(
    root,
    text = "Experimental Design",
    font = ("Arial", 16),
    bg = "green",
    command = show_info_button_3,
    width = 30
)
button_3.grid(row = 3, column = 1, padx = 10, pady = 5)

#End of information window 3

#Start of Information window 4
def show_info_button_4():

    info_window = tk.Toplevel(root)

    info_window.title("Experimental Results")
    info_window.geometry("2395x1200")

    #adding information to the popup window
    title = tk.Label(
        info_window,
        text = "Experimental Results",
        font = ("Arial", 16, "bold")
    )
    title.pack(pady=10)

    #inserting the image
    # Open image file
    image = Image.open("Slug Cartoon.jpeg")

    # Resize image (width, height)
    image = image.resize((400, 300))

    # Convert image for Tkinter
    photo = ImageTk.PhotoImage(image)

    # Create label to display image
    image_label = tk.Label(info_window, image=photo)

    # Keep a reference to prevent image disappearing
    image_label.image = photo

    # Add image to window
    image_label.pack(pady=10)

    #end of inserting in the image

    info_text = """
    In short, based on the results of peer reviewed research my team was able to conclude that higher moisture generally appears to support greater amounts of nematodes and persistence in slug environments. In more simple terms, slugs that are found closer to water rich environments are more likely to have a greater population of nematodes, and have more resilient, long living nematodes.  

    Grant and Villani (2003) demonstrated that entomopathogenic nematodes performed substantially better under wetter soil conditions. Further this peer reviewed article showed that Nematode Virulence (how effective they are at killing slugs) increased as soil moisture increased. This study also found that nematodes require a certain amount of water for movement and can become dormant under dry conditions, however rehydrating them restored their virulence capabilities.   

    Nermut et al. (2024) found that slug parasitic nematodes are typically applied in agriculture via being suspended in water and directed into moist soil environments. This peer reviewed study went on to display that nematodes establish and interact with slugs stronger under moist conditions. In short, the moister the conditions, the greater the interaction between slug and nematode.   
    
    Sudhaus (2018) found that snails and slugs alike commonly harbor many unique nematode species. Across 158 gastropods, 78% contained non-parasitic nematodes (nematodes not killing the slugs and snails) and as many as 16 nematode species were found in a single species of slug. This study also showed that gastropods collected in drought related conditions often lacked nematodes in their intestines.   

    
    Reference Page:  

    Sudhaus, W. (2018). Dispersion of nematodes (Rhabditida) in the guts of slugs and snails. Soil Organisms, 90(3), 101–114. doi:10.25674/4jp6-0v30  

    Grant, J. A., M. G. Villani. (2003) Soil Moisture Effects on entomopathogenic Nematodes. Environmental Entomology, Volume 32, Issue 1, 1. pages 80-87. Doi: https://doi.org/10.1603/0046-225X-32.1.80  

    Nermuť, J., Konopická, J., Weijler, V. et al. The use of Phasmarhabditis nematodes and metabolites of Xenorhabdus bacteria in slug control. Appl Microbiol Biotechnol 108, 8 (2024). https://doi.org/10.1007/s00253-023-12886-6  
    
    """

    info_label = tk.Label(
        info_window,
        text = info_text,
        justify = "left",
        wraplength = 450
    )

    info_label.pack(padx = 20, pady = 10)


#code for actual button for information window 4
button_4 = tk.Button(
    root,
    text = "Experimental Results",
    font = ("Arial", 16),
    bg = "green",
    command = show_info_button_4,
    width = 30
)
button_4.grid(row = 4, column = 1, padx = 10, pady = 5)


#End of Information window 4

#Start of Information window 5
def show_info_button_5():

    info_window = tk.Toplevel(root)

    info_window.title("Research Conclusion")
    info_window.geometry("2395x1200")

    #adding information to the popup window
    title = tk.Label(
        info_window,
        text = "Research Conclusion",
        font = ("Arial", 16, "bold")
    )
    title.pack(pady=10)

    #inserting the image
    # Open image file
    image = Image.open("Slug_Conclusion.jpeg")

    # Resize image (width, height)
    image = image.resize((400, 300))

    # Convert image for Tkinter
    photo = ImageTk.PhotoImage(image)

    # Create label to display image
    image_label = tk.Label(info_window, image=photo)

    # Keep a reference to prevent image disappearing
    image_label.image = photo

    # Add image to window
    image_label.pack(pady=10)

    #end of inserting in the image

    info_text = """
    After conduction extensive research on what effect does water have on nematode richness in slugs? My group has been able to determine that nematode richness is directly correlated to water abundance. If for instance you were able to increase the amount of water around where a slug was located, over a period you would also see an increase in nematode richness.  

    From Sudhaus (2018) slugs harbor many nematodes in their intestines however their amount and richness are directly connected to if the slug is found in a wet or dry environment. From Nermut et al (2024) the interaction between slugs and nematodes increases in strength. The moister the environment is that surrounds a slug. And finally, from Grant and Villani (2003) one can see that nematodes require a certain amount of water to move and function properly. Further, this study went on to suggest that nematode virulence increased as soil moisture increased.  

    This means that our team can conclude that our hypothesis and predication were correct. Yes, if you take a slug from a place closer to running water, you will find an abundance of effective nematodes. However, this research also bounds our hypothesis and prediction. It appears that whether the water is running or not does not entirely matter, only the presence and amount of water truly matters. 
    """

    info_label = tk.Label(
        info_window,
        text = info_text,
        justify = "left",
        wraplength = 450
    )

    info_label.pack(padx = 20,pady = 10)


#code for actual button for information window 3
button_5 = tk.Button(
    root,
    text = "Research Conclusion",
    font = ("Arial", 16),
    bg = "green",
    command = show_info_button_5,
    width = 30
)
button_5.grid(row = 5, column = 1, padx = 10, pady = 5)


#End of information window 5 

#creating a reference page button so people can see the peer reviewed research documents themselves
#function below is the comand associated with the reference page button later in the file
def reference_page():

    info_window = tk.Toplevel(root)

    info_window.title("Reference Page")
    info_window.geometry("2395x1200")

    #adding information to the popup window
    title = tk.Label(
        info_window,
        text = "Reference Page",
        font = ("Arial", 16, "bold")
    )
    title.pack(pady=10)

    #inserting the image
    # Open image file
    image = Image.open("Slug_Conclusion.jpeg")

    # Resize image (width, height)
    image = image.resize((400, 300))

    # Convert image for Tkinter
    photo = ImageTk.PhotoImage(image)

    # Create label to display image
    image_label = tk.Label(info_window, image=photo)

    # Keep a reference to prevent image disappearing
    image_label.image = photo

    # Add image to window
    image_label.pack(pady=10)

    #end of inserting in the image

    info_text = """

    Citation 1:
        - Sudhaus, W. (2018). Dispersion of nematodes (Rhabditida) in the guts of slugs and snails. Soil Organisms, 90(3), 101–114. doi:10.25674/4jp6-0v30  

    Citation 2:
        - Grant, J. A., M. G. Villani. (2003) Soil Moisture Effects on entomopathogenic Nematodes. Environmental Entomology, Volume 32, Issue 1, 1. pages 80-87. Doi: https://doi.org/10.1603/0046-225X-32.1.80  

    Citation 3:
        - Nermuť, J., Konopická, J., Weijler, V. et al. The use of Phasmarhabditis nematodes and metabolites of Xenorhabdus bacteria in slug control. Appl Microbiol Biotechnol 108, 8 (2024). https://doi.org/10.1007/s00253-023-12886-6  
  
    """

    info_label = tk.Label(
        info_window,
        text = info_text,
        justify = "left",
        wraplength = 450
    )

    info_label.pack(padx = 20,pady = 10)

#code that actually creates the reference button
reference_page_button = tk.Button(
    root,
    text = "Reference Page",
    font = ("Arial", 16), 
    command = reference_page,
    bg = "green",
    width = 30
)

#placing the reference page on the homepage grid for stylistic purposes and organization
reference_page_button.grid(row = 6, column = 0, padx = 10, pady = 5)

#end of reference page button

#function that actually opens the window and runs the code
root.mainloop()