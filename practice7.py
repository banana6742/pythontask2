from bs4 import BeautifulSoup

book_shop_doc="""
<catalog>

<head>
    <title>The web book catalog</title></head>
    <p class="title"><b>The Book Catalog</b></p>
<books>
    <book id="bk001">
        <Author>HighTower</Author>
        <genre>Fiction</genre>
        <price>44.34</price>
        <pub_date>2000-10-10</pub_date>
        <review>An Amazing story of nothing.</review>
    </book>


    <book id="bk002">
        <Author>Nagata,Suanne</Author>
        <title>Becoming somebody</title>
        <genre>Biography</genre>
        <review>A masterPiece of the art</review>
    </book>

    <book id="bk003">
        <Author>Oberg,Bruce</Author>
        <title>The Poet's First Poem</title>
        <genre>poem</genre>
        <price>28.2</price>
        <review>The Least Poetic Poems</review>
    </book>
        
</books>

</catalog>
    
"""
book_soup = BeautifulSoup(book_shop_doc,"html.parser")

print(book_soup)

print("-"*50)

for string in book_soup.stripped_strings:
    print(repr(string))

print('__________parents__________')

element_soup=book_soup.catalog.books
print(element_soup)

print("-"*50)

next_element= element_soup.next_element.next_element
print(next_element)

print('--------------')
next_sibling = book_soup.catalog.books.book
print(next_sibling)

print('--------------')
previous_element= next_element.previous_element.previous_element
print(previous_element)

print('--------------')
#navigator to next sibling
next_sibling2= next_sibling.next_sibling
print(next_sibling2.next_sibling)

print('--------------')
#navigate to previous sibling
previous_sibling=next_sibling2.previous_sibling
print(previous_sibling)