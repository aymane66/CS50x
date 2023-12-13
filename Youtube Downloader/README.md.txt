# YouTube Video Downloader
#### Video Demo: [Watch Demo](<URL HERE>)
#### Description:

The YouTube Video Downloader is a web application designed to simplify the process of fetching and downloading YouTube videos. With an intuitive interface,
users can easily input a YouTube URL, retrieve video thumbnail, and download the desired content in various resolutions. The application is built using Django,
Pytube, and incorporates responsive design for an optimal user experience on different devices.

## Features:

1. **User-Friendly Interface:**
   - The application provides a straightforward interface for users to paste YouTube URLs and initiate video fetching and downloading processes.

2. **Video Fetching:**
   - Users can fetch details about a YouTube video, including its title, thumbnail, and available resolutions for download.

3. **Resolution Selection:**
   - After fetching video details, users can choose their preferred resolution from the available options before initiating the download.

4. **Responsive Design:**
   - The frontend is designed with responsiveness in mind, ensuring a seamless experience across various screen sizes and devices.


## Project Structure:

### `views.py`
The backend logic is put in the `views.py` file, which defines a Django class-based view named `home`. This view handles both GET and POST requests,
managing the rendering of the initial HTML page and processing form submissions.

### `home.html`
The main HTML template, `home.html`, provides the structure for the user interface. It includes a form for inputting YouTube URLs, dynamic content display
for fetched video details, and resolution selection buttons.

### `styles.css`
Styling is managed in the `styles.css` file, enhancing the visual appeal of the web interface. The CSS includes styles for form elements, buttons, and image
hover effects, contributing to an engaging user experience.


## Usage:

1. **Input YouTube URL:**
   - Open the application in a web browser.
   - Paste a valid YouTube URL into the provided input field.

2. **Fetch Video Details:**
   - Click the "Fetch Video" button to retrieve details about the video.

3. **Select Resolution:**
   - After fetching details, select a preferred resolution from the available options, and the video starts downloading.

4. **Download Success:**
   - Upon successful download, a confirmation message will be displayed.

## Note:
- Ensure that Django and Pytube dependencies are installed before running the application.
- Customize and modify the code to meet specific requirements or address issues.
- If you encounter any challenges or have suggestions for improvements, refer to the project's issue tracker for assistance. Enjoy using
the YouTube Video Downloader!
