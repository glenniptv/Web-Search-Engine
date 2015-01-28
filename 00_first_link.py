#A very rough draft for crawler
#Tries to search for a link on web-page by searching for <a href="...."
page = #content of some web page
start_link = page.find('<a href=')
start_quote = page.find('"', start_link)
end_quote = page.find('"', start_quote + 1)
link = page[start_quote+1:end_quote]
