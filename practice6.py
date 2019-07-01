from bs4 import BeautifulSoup as Bs

school="""
<address>

<head>
    <title>This is spice up academy</title>
</head>

<body>
    
<schools>
    <p class="title">
        <b>This is located in the heart of Bangalore city koramangala</b>
    </p>

    <classrooms>
        <classroom id="555F">
            <teacher>Lohith</teacher>
            <subject>Python And Machine Learning</subject>
            <dob>30/10/1994</dob>
            <date>30-11-2019</date>
            <review>Amazing to study with you</review>
        </classroom>

        <good id="666F">
            <teacher>Susumu</teacher>
            <subject>Php And Machine Learning</subject>
            <dob>01/10/1991</dob>
            <date>30-11-2019</date>
            <review>Bangalore study with you</review>
        </good>

        <bad id="777F">
                <teacher>Koyota</teacher>
                <subject>Ruby And Machine Learning</subject>
                <dob>01/10/1998</dob>
                <date>04-10-2012</date>
                <review>Good to meet you and to study with you</review>
        </bad>
            

    </classrooms>

</schools>

<ok>
    <p>hiegaga</p>
    <h1>egoweut3yqeh</h1>
    <p>hiegaga</p>
</ok>

</body>
</address>"""

ss = Bs(school,'html.parser')
print(ss)

print('-'*50)
print(ss.contents)


print('-'*50)
print('='*50)

print(ss.address)

print('-'*50)
print('='*50)

print(ss.head)

print('-'*50)
print('='*50)

title_tag=ss.title
print(title_tag)
print('-'*50)
print('='*50)

for me in ss.head.descendants:
    print(me)
print('-'*50)
print('='*50)

for me in ss.teacher.descendants:
    print(repr(me))

print('-'*50)
print('='*50)

print(title_tag.parent)

print('-'*50)
print('='*50)

navigate_up = ss.subject
print(navigate_up)
print('-'*50)
print('='*50)


for me in navigate_up.stripped_strings:
    print(repr(me))
print('@'*50)

back_and_forth = ss.address.bad
print(back_and_forth)
print('-'*50)
print('='*50)

o = back_and_forth.next_element.next_element
print(o)

ok = back_and_forth.next_element.next_element.next_element
print(ok)

okk=ok.next_element.next_element.next_element.next_element.next_element
print(okk)

okkk=okk.next_element
print(okkk)

print('-'*50)
print('='*50)

select_ok_tag=ss.ok
print(select_ok_tag)

print('-'*50)
print('='*50)

ok_tag_saving_here=select_ok_tag.next_element.next_element
print(ok_tag_saving_here)
print('-'*50)
print('='*50)

next=ss.ok.p
print(next)

nex = next.next_element.next_element
print(nex)
