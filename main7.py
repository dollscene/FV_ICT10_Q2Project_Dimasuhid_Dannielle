from pyscript import document, display

# --- DICTIONARY FOR CLUBS ---
clubs = {
    "Marching Band": {
        "desc": "Leading the school spirit through musical precision.",
        "time": "Tuesday & Wednesday 03:00-4:30 PM",
        "loc": "Band Room",
        "mod": "Mr. Emilio Alumno",
        "mem": "45 Members",
        "cat": "Performing Arts"
    },
    "Glee Club": {
        "desc": "The official school choir and vocal ensemble.",
        "time": "Monday 03:00-05:00 PM",
        "loc": "HS Music Room",
        "mod": "Mr. Denver Martin",
        "mem": "30 Members",
        "cat": "Performing Arts"
    },
    "Math Club": {
        "desc": "Challenging students through logic and advanced puzzles.",
        "time": "Monday 02:30-03:00 PM",
        "loc": "Room 404",
        "mod": "Mr. Nicole Gabuya",
        "mem": "15 Members",
        "cat": "Academic"
    },
    "Science Club": {
        "desc": "Hands-on experiments and environmental research.",
        "time": "Tuesday 03:00-04:00 PM",
        "loc": "Room 404",
        "mod": "Ms. Jameelyn Maramag",
        "mem": "22 Members",
        "cat": "Academic"
    },
    "Volleyball": {
        "desc": "Developing teamwork and athletic excellence.",
        "time": "Wednesday 03:00-04:00 PM",
        "loc": "Quadrangle",
        "mod": "Mr. Adrian Ruiz",
        "mem": "14 Members",
        "cat": "Athletics"
    }
}

# --- CLUB LOGIC ---
def show_club_info(event):
    selection = document.getElementById("club_select").value
    welcome = document.getElementById("welcome_msg")
    display_div = document.getElementById("club_display")

    if selection in clubs:
        welcome.style.display = "none"
        display_div.style.display = "block"
        data = clubs[selection]
        
        document.getElementById("out_name").innerText = selection
        document.getElementById("out_desc").innerText = data["desc"]
        document.getElementById("out_mod").innerText = data["mod"]
        document.getElementById("out_time").innerText = data["time"]
        document.getElementById("out_loc").innerText = data["loc"]
        document.getElementById("out_mem").innerText = data["mem"]
        document.getElementById("out_cat").innerText = data["cat"]
    else:
        welcome.style.display = "block"
        display_div.style.display = "none"

# --- GWA LOGIC ---
def general_weighted_average(event):
    try:
        first_name = document.getElementById('first_name').value
        last_name = document.getElementById('last_name').value

        # Grades input
        s = float(document.getElementById('science_grade').value)
        m = float(document.getElementById('math_grade').value)
        e = float(document.getElementById('english_grade').value)
        f = float(document.getElementById('filipino_grade').value)
        i = float(document.getElementById('ict_grade').value)
        p = float(document.getElementById('pe_grade').value)

        weighted_sum = (s * 5 + m * 5 + e * 5 + f * 3 + i * 2 + p * 1)
        gwa = weighted_sum / 21

        # Updated Modern Output
        document.getElementById('gwa_result_card').style.display = "block"
        document.getElementById('res_full_name').innerText = f"{first_name} {last_name}"
        document.getElementById('res_gwa_value').innerText = f"{gwa:.2f}"
        
    except Exception as err:
        document.getElementById('res_full_name').innerText = "Error: Please check grades."