# Freebnbnow

![Freebnbnow Image](https://github.com/user-attachments/assets/d9cb583f-649f-4f2c-bd6d-db694f794635)

Freebnbnow is a robust Python tool designed to automate the process of claiming Mining Speed every hour, allowing you to effortlessly boost your BNB mining potential. With its intuitive interface and dependable performance, this tool is ideal for users looking to streamline and optimize their mining activities.

## Key Features
- **Real-Time Feedback**: Get real-time updates on the status of your claims and any potential issues.
- **User-Friendly Interface**: Simple and intuitive interface powered by the `rich` library.
- **Automated Mining Speed Claims**: Automatically claim 25 TH/S every hour.
- **Secure Cookie Management**: Safely input and manage your session cookies.
- **Error Handling**: Comprehensive error messages to guide you through any problems.

## Installation
1. **Clone the Repository:**
    ```
    $ git clone https://github.com/RozhakXD/Freebnbnow.git
    $ cd Freebnbnow
    ```
2. **Install the Required Libraries:**
    ```
    pip install requests rich
    ```

## Usage
1. **Run the Program:**
    ```
    python Run.py
    ```
2. **Input Your Cookies**: When prompted, enter your freebnbnow account cookies. Ensure you are logged in and that your cookies are valid. You can use tools like [Via Browser](https://play.google.com/store/apps/details?id=mark.via.gp&hl=id) to obtain your cookies.
3. **Let It Run**: The tool will automatically claim Mining Speed for you every hour. Monitor the console for real-time updates and follow any instructions provided.

## Troubleshooting
- **Stuck at "WAIT X SECOND!"**: If the program is stuck counting down the seconds but doesn't proceed, your session may have expired. Restart the program and input fresh cookies.
- **Invalid Cookies**: If you receive an error stating that the cookies are incorrect, double-check that you have copied the correct SESSION cookie from your browser. Ensure that it contains session= and try again.
- **Connection Issues**: If you see a message about connection problems, ensure that your internet connection is stable. The program will retry after 10 seconds.
- **Mining Speed Not Claimed**: If the mining speed isn't claimed even after the countdown, this could be due to a temporary issue with the Freebnbnow website. Wait a few minutes and try again.

## Screenshot
![FunPic_20240823](https://github.com/user-attachments/assets/d340070b-44dc-41b6-9aa7-3a0676079dc9)

## Notes
- **Stopping the Program**: You can stop the program at any time by pressing `CTRL + Z`. If the program gets stuck, use `CTRL + C` to terminate it.
- **Session Expiration**: If an error occurs, it may be due to expired cookies. Simply restart the program and input new cookies.

## Support
If you find this tool helpful, consider supporting the development via [PayPal](https://paypal.me/rozhak9) or [Trakteer](https://trakteer.id/rozhak_official/tip).
