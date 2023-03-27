# Flight-Club
Flight Club is a Python program that checks for the cheapest flights from a given city to a list of destinations stored in a Google Sheet. If the price is lower than the lowest price listed in the sheet, it sends an SMS message and email to notify the user.

## Installation
1. Clone the repository to your local machine:

        git clone https://github.com/Siddharth-2382/Flight-Club.git
2. Install the required Python packages:

        cd Flight-Club
        pip install -r requirements.txt
3. Create a .env file in the root directory of the project with the following variables:

        ORIGIN_CITY_IATA=<YOUR_ORIGIN_CITY_IATA_CODE>
        TEQUILA_ENDPOINT=https://tequila-api.kiwi.com
        TEQUILA_API_KEY=<YOUR_TEQUILA_API_KEY>
        SHEETY_PRICES_ENDPOINT=<YOUR_SHEETY_PRICES_API_ENDPOINT>
        SHEETY_USERS_ENDPOINT=<YOUR_SHEETY_USERS_API_ENDPOINT>
        SHEETY_USERNAME=<YOUR_SHEETY_USERNAME>
        SHEETY_PASSWORD=<YOUR_SHEETY_PASSWORD>
        TWILIO_SID=<YOUR_TWILIO_ACCOUNT_SID>
        TWILIO_AUTH_TOKEN=<YOUR_TWILIO_AUTH_TOKEN>
        MY_EMAIL=<YOUR_EMAIL_ADDRESS>
        MY_PASSWORD=<YOUR_EMAIL_PASSWORD>
        TWILIO_NUMBER=<YOUR_TWILIO_PHONE_NUMBER>
        MY_NUMBER=<YOUR_PHONE_NUMBER>
## Usage
To run the program, simply execute the `main.py` file:

        python main.py
The program will check for the cheapest flights from your origin city to each destination in the Google Sheet. If the price is lower than the lowest price listed in the sheet, it will send an SMS and email to notify you of the deal.
## Credits
Flight Club was created by me using the Flight Search and Sheety APIs from Kiwi.com, and the Twilio API for SMS messaging. 

## Note
Format your Google Sheet corresponding to the `SHEETY_PRICES_ENDPOINT` in the following manner keeping IATA Code column empty:

![image](https://user-images.githubusercontent.com/94699055/227850394-7af50221-d7cf-4cac-a747-b7de322c49ef.png)


The `main.py` script will find the IATA codes for the respective destinations and insert it in the respective cells as shown below.

![2020-07-30_14-17-49-541979e0b7b1edbc9eb6c32e9794ea56](https://user-images.githubusercontent.com/94699055/227850730-fd58b99d-6042-4db6-adac-c5ddf270f871.gif)

Format your Google Sheet correspoding to the `SHEETY_USERS_ENDPOINT` in the following manner:

![image](https://user-images.githubusercontent.com/94699055/227853718-a7cdb2ef-c614-4bca-9308-fab3399015d3.png)

You can fill these sheet manually or run the `fill_user_details.py` repeatedly to fill it from your terminal.

---


