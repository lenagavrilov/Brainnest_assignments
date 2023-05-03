''' The goal of this project is to create a weather app that shows the current weather conditions
and forecast for a specific location.

Here are the steps you can take to create this project:

    Use the requests library to make an API call to a weather service (e.g. OpenWeatherMap)
    to retrieve the weather data for a specific location.

    Use the json library to parse the JSON data returned by the API call.

    Use the tkinter library to create a GUI for the app, including widgets such as labels, buttons and text boxes.

    Use the Pillow library to display the weather icons.

    Use the datetime library to display the current time and date. '''

from tkinter import *
from tkinter import messagebox, ttk
from configparser import ConfigParser
import requests
from datetime import datetime
from PIL import ImageTk, Image
from urllib.request import urlopen


class WeatherApp(Tk):
    def __init__(self):
        super().__init__()
        self.title("Weather App")
        self.geometry('700x500')

        self.url = 'https://api.openweathermap.org/data/2.5/weather?q={}&appid={}'
        self.api_key = self.get_api_key()
        self.lbl_city = StringVar()
        self.lbl_country = StringVar()
        self.countries_index = self.get_countries()

        self.create_gui()


    def create_gui(self):
        self.request_city_frame = Frame()
        self.request_city_frame.pack()

        self.request_country_frame = Frame()
        self.request_country_frame.pack()

        self.frame_bottom = Frame()
        self.frame_bottom.pack(side=BOTTOM)

        self.lbl_ask_city = Label(self.request_city_frame,text='Enter city:', font=('Arial', 15))
        self.lbl_ask_city.pack(side=LEFT)

        self.ent_city = Entry(self.request_city_frame, textvariable=self.lbl_city, font=('Arial', 15))
        self.ent_city.focus()
        self.ent_city.pack(side=LEFT, padx= 10)

        self.lbl_ask_country = Label(self.request_country_frame, text='Enter country:', font=('Arial', 15))
        self.lbl_ask_country.pack(side=LEFT)

        self.countries = ttk.Combobox(self.request_country_frame,
                                      values = list(self.countries_index.values()),
                                      font=('Arial', 15),
                                      textvariable=self.lbl_country
                                      )
        self.countries.pack(side=LEFT)

        self.btn_search = Button(text="Search weather", command=self.search, width=20, font=('Arial', 15))
        self.btn_search.pack()

        self.lbl_location = Label(text="", font=('bold',30))
        self.lbl_location.pack()

        self.lbl_image = Label(image='')
        self.lbl_image.pack()

        self.lbl_temperature = Label(text='', font=('Arial', 20))
        self.lbl_temperature.pack()

        self.lbl_feels_like = Label(text='', font=('Arial', 20))
        self.lbl_feels_like.pack()

        self.lbl_wind_speed= Label(text='', font=('Arial', 20))
        self.lbl_wind_speed.pack()

        self.lbl_weather = Label( text='',  font=('Arial', 20))
        self.lbl_weather.pack()

        self.lbl_updated = Label(self.frame_bottom, text='', font=('Arial', 10))
        self.lbl_updated.pack()

    def get_countries(self):
        return {
                 "AF": "Afghanistan",
                 "AX": "Aland Islands",
                 "AL": "Albania",
                 "DZ": "Algeria",
                 "AS": "American Samoa",
                 "AD": "Andorra",
                 "AO": "Angola",
                 "AI": "Anguilla",
                 "AQ": "Antarctica",
                 "AG": "Antigua and Barbuda",
                 "AR": "Argentina",
                 "AM": "Armenia",
                 "AW": "Aruba",
                 "AU": "Australia",
                 "AT": "Austria",
                 "AZ": "Azerbaijan",
                 "BS": "Bahamas",
                 "BH": "Bahrain",
                 "BD": "Bangladesh",
                 "BB": "Barbados",
                 "BY": "Belarus",
                 "BE": "Belgium",
                 "BZ": "Belize",
                 "BJ": "Benin",
                 "BM": "Bermuda",
                 "BT": "Bhutan",
                 "BO": "Bolivia, Plurinational State of",
                 "BQ": "Bonaire, Sint Eustatius and Saba",
                 "BA": "Bosnia and Herzegovina",
                 "BW": "Botswana",
                 "BV": "Bouvet Island",
                 "BR": "Brazil",
                 "IO": "British Indian Ocean Territory",
                 "BN": "Brunei Darussalam",
                 "BG": "Bulgaria",
                 "BF": "Burkina Faso",
                 "BI": "Burundi",
                 "KH": "Cambodia",
                 "CM": "Cameroon",
                 "CA": "Canada",
                 "CV": "Cape Verde",
                 "KY": "Cayman Islands",
                 "CF": "Central African Republic",
                 "TD": "Chad",
                 "CL": "Chile",
                 "CN": "China",
                 "CX": "Christmas Island",
                 "CC": "Cocos (Keeling) Islands",
                 "CO": "Colombia",
                 "KM": "Comoros",
                 "CG": "Congo",
                 "CD": "Congo, The Democratic Republic of the",
                 "CK": "Cook Islands",
                 "CR": "Costa Rica",
                 "CI": "Côte d'Ivoire",
                 "HR": "Croatia",
                 "CU": "Cuba",
                 "CW": "Curaçao",
                 "CY": "Cyprus",
                 "CZ": "Czech Republic",
                 "DK": "Denmark",
                 "DJ": "Djibouti",
                 "DM": "Dominica",
                 "DO": "Dominican Republic",
                 "EC": "Ecuador",
                 "EG": "Egypt",
                 "SV": "El Salvador",
                 "GQ": "Equatorial Guinea",
                 "ER": "Eritrea",
                 "EE": "Estonia",
                 "ET": "Ethiopia",
                 "FK": "Falkland Islands (Malvinas)",
                 "FO": "Faroe Islands",
                 "FJ": "Fiji",
                 "FI": "Finland",
                 "FR": "France",
                 "GF": "French Guiana",
                 "PF": "French Polynesia",
                 "TF": "French Southern Territories",
                 "GA": "Gabon",
                 "GM": "Gambia",
                 "GE": "Georgia",
                 "DE": "Germany",
                 "GH": "Ghana",
                 "GI": "Gibraltar",
                 "GR": "Greece",
                 "GL": "Greenland",
                 "GD": "Grenada",
                 "GP": "Guadeloupe",
                 "GU": "Guam",
                 "GT": "Guatemala",
                 "GG": "Guernsey",
                 "GN": "Guinea",
                 "GW": "Guinea-Bissau",
                 "GY": "Guyana",
                 "HT": "Haiti",
                 "HM": "Heard Island and McDonald Islands",
                 "VA": "Holy See (Vatican City State)",
                 "HN": "Honduras",
                 "HK": "Hong Kong",
                 "HU": "Hungary",
                 "IS": "Iceland",
                 "IN": "India",
                 "ID": "Indonesia",
                 "IR": "Iran, Islamic Republic of",
                 "IQ": "Iraq",
                 "IE": "Ireland",
                 "IM": "Isle of Man",
                 "IL": "Israel",
                 "IT": "Italy",
                 "JM": "Jamaica",
                 "JP": "Japan",
                 "JE": "Jersey",
                 "JO": "Jordan",
                 "KZ": "Kazakhstan",
                 "KE": "Kenya",
                 "KI": "Kiribati",
                 "KP": "Korea, Democratic People's Republic of",
                 "KR": "Korea, Republic of",
                 "KW": "Kuwait",
                 "KG": "Kyrgyzstan",
                 "LA": "Lao People's Democratic Republic",
                 "LV": "Latvia",
                 "LB": "Lebanon",
                 "LS": "Lesotho",
                 "LR": "Liberia",
                 "LY": "Libya",
                 "LI": "Liechtenstein",
                 "LT": "Lithuania",
                 "LU": "Luxembourg",
                 "MO": "Macao",
                 "MK": "Macedonia, Republic of",
                 "MG": "Madagascar",
                 "MW": "Malawi",
                 "MY": "Malaysia",
                 "MV": "Maldives",
                 "ML": "Mali",
                 "MT": "Malta",
                 "MH": "Marshall Islands",
                 "MQ": "Martinique",
                 "MR": "Mauritania",
                 "MU": "Mauritius",
                 "YT": "Mayotte",
                 "MX": "Mexico",
                 "FM": "Micronesia, Federated States of",
                 "MD": "Moldova, Republic of",
                 "MC": "Monaco",
                 "MN": "Mongolia",
                 "ME": "Montenegro",
                 "MS": "Montserrat",
                 "MA": "Morocco",
                 "MZ": "Mozambique",
                 "MM": "Myanmar",
                 "NA": "Namibia",
                 "NR": "Nauru",
                 "NP": "Nepal",
                 "NL": "Netherlands",
                 "NC": "New Caledonia",
                 "NZ": "New Zealand",
                 "NI": "Nicaragua",
                 "NE": "Niger",
                 "NG": "Nigeria",
                 "NU": "Niue",
                 "NF": "Norfolk Island",
                 "MP": "Northern Mariana Islands",
                 "NO": "Norway",
                 "OM": "Oman",
                 "PK": "Pakistan",
                 "PW": "Palau",
                 "PS": "Palestinian Territory, Occupied",
                 "PA": "Panama",
                 "PG": "Papua New Guinea",
                 "PY": "Paraguay",
                 "PE": "Peru",
                 "PH": "Philippines",
                 "PN": "Pitcairn",
                 "PL": "Poland",
                 "PT": "Portugal",
                 "PR": "Puerto Rico",
                 "QA": "Qatar",
                 "RE": "Réunion",
                 "RO": "Romania",
                 "RU": "Russian Federation",
                 "RW": "Rwanda",
                 "BL": "Saint Barthélemy",
                 "SH": "Saint Helena, Ascension and Tristan da Cunha",
                 "KN": "Saint Kitts and Nevis",
                 "LC": "Saint Lucia",
                 "MF": "Saint Martin (French part)",
                 "PM": "Saint Pierre and Miquelon",
                 "VC": "Saint Vincent and the Grenadines",
                 "WS": "Samoa",
                 "SM": "San Marino",
                 "ST": "Sao Tome and Principe",
                 "SA": "Saudi Arabia",
                 "SN": "Senegal",
                 "RS": "Serbia",
                 "SC": "Seychelles",
                 "SL": "Sierra Leone",
                 "SG": "Singapore",
                 "SX": "Sint Maarten (Dutch part)",
                 "SK": "Slovakia",
                 "SI": "Slovenia",
                 "SB": "Solomon Islands",
                 "SO": "Somalia",
                 "ZA": "South Africa",
                 "GS": "South Georgia and the South Sandwich Islands",
                 "ES": "Spain",
                 "LK": "Sri Lanka",
                 "SD": "Sudan",
                 "SR": "Suriname",
                 "SS": "South Sudan",
                 "SJ": "Svalbard and Jan Mayen",
                 "SZ": "Swaziland",
                 "SE": "Sweden",
                 "CH": "Switzerland",
                 "SY": "Syrian Arab Republic",
                 "TW": "Taiwan, Province of China",
                 "TJ": "Tajikistan",
                 "TZ": "Tanzania, United Republic of",
                 "TH": "Thailand",
                 "TL": "Timor-Leste",
                 "TG": "Togo",
                 "TK": "Tokelau",
                 "TO": "Tonga",
                 "TT": "Trinidad and Tobago",
                 "TN": "Tunisia",
                 "TR": "Turkey",
                 "TM": "Turkmenistan",
                 "TC": "Turks and Caicos Islands",
                 "TV": "Tuvalu",
                 "UG": "Uganda",
                 "UA": "Ukraine",
                 "AE": "United Arab Emirates",
                 "GB": "United Kingdom",
                 "US": "United States",
                 "UM": "United States Minor Outlying Islands",
                 "UY": "Uruguay",
                 "UZ": "Uzbekistan",
                 "VU": "Vanuatu",
                 "VE": "Venezuela, Bolivarian Republic of",
                 "VN": "Viet Nam",
                 "VG": "Virgin Islands, British",
                 "VI": "Virgin Islands, U.S.",
                 "WF": "Wallis and Futuna",
                 "YE": "Yemen",
                 "ZM": "Zambia",
                 "ZW": "Zimbabwe"
            }

    def get_api_key(self):
        config_file = 'config.ini'
        config = ConfigParser()
        config.read(config_file)
        api_key = config['api_key']['key']
        return api_key

    def get_image(self, img):
        url_img = 'https://openweathermap.org/img/w/{}.png'.format(img)
        try:
            data = urlopen(url_img)
        except:
            pass
        return ImageTk.PhotoImage(data=data.read())

    def search(self):
        city = self.lbl_city.get()
        country = self.lbl_country.get()
        if country:
            country_key_get = [i for i in self.countries_index if self.countries_index[i] == country]
        else:
            country_key_get = []

        if country_key_get:
            country_key = country_key_get[0]
        else:
            country_key = ''

        current_weather = self.get_weather(city, country_key)
        if current_weather:
            self.lbl_location['text'] = '{}, {}'.format(current_weather[0], current_weather[1])
            self.image = self.get_image(current_weather[5])
            self.lbl_image['image'] = self.image
            self.lbl_temperature['text'] = 'Temperature: {:.0f} °C'.format(current_weather[2])
            self.lbl_feels_like['text'] = 'Feels like: {:.0f} °C'.format(current_weather[3])
            self.lbl_wind_speed['text'] = 'Wind Speed: ' + str(current_weather[4]) + ' meter/sec'
            self.lbl_weather['text'] = current_weather[6]
            self.lbl_updated['text'] = 'Last updated: {}'.format(current_weather[7])
        else:
            if country:
                messagebox.showerror('Error', 'Cannot find city {} in  {}'.format(city, country))
            else:
                messagebox.showerror('Error', 'Cannot find city {}'.format(city))

    def get_weather(self, city, country_key):
        if not self.api_key:
            messagebox.showerror('Error', 'Missing api key')
        else:
            try:
                result = requests.get(self.url.format(city +',' + country_key, self.api_key))
                if result:
                    json = result.json()
                    city = json['name']
                    country = json['sys']['country']
                    temp_kelvin = json['main']['temp']
                    temp_celsius = temp_kelvin - 273.15
                    temp_kelvin_feels = json['main']['feels_like']
                    temp_celsius_feels = temp_kelvin_feels - 273.15
                    icon = json['weather'][0]['icon']
                    weather = json['weather'][0]['main']
                    wind_speed = json['wind']['speed']
                    updated_unix = json['dt']
                    updated = datetime.fromtimestamp(updated_unix)
                    updated  = updated.strftime('%d/%m/%Y %H:%M')
                    data = (city, country, temp_celsius, temp_celsius_feels,  wind_speed, icon, weather, updated)
                    return data
                else:
                    return None
            except:
                messagebox.showerror('Error', 'Cannot retrieve data now. Try later')


if __name__ == '__main__':
    app = WeatherApp()
    app.mainloop()
