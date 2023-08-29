url = "https://github.com/bcaffo/courses.git"
urlConnection = url.openConnection();
urlConnection.connect();
int_file_size = urlConnection.getContentLength();
print(int_file_size)