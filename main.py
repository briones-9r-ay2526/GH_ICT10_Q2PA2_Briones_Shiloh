# Participation Activity: Working with Sets
from pyscript import display, document


def add_name(e):
    document.getElementById('output').innerHTML = ' '

    #  Sets Variable
    seven = {'Adarna Ibon', 'Don Juan de la Cruz', 'Don Diego de la Cruz', 'Don Pedro de la Cruz'}
    eight = {'Florante Flores', 'Laura Lopez', 'Aladin Alcaraz', 'Adolfo Adecer'}
    nine = {'Crisostomo Ibarra', 'Maria Clara de los Santos', 'Elias Esguerra'}
    ten = {'Simoun Ibarra', 'Basilio Briones', 'Isagani Irinco', 'Juli Hernandez'}

    fname = document.getElementById('fname').value.title().strip()
    lname = document.getElementById('lname').value.title().strip()

    # Creates Master List and Adds User Input
    members = (seven | eight | nine | ten)
    members.add(fname + lname)

    # Displays
    display(f'Congratulations {fname} {lname}! Welcome to the OBMC Social Studies Club.', target='output')

    display(f'List of members: {members}. Total number of members: {len(members)}', target='output')
    display(f'Total number of members: {len(members)}', target='output')