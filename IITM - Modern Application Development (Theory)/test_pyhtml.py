import pyhtml as p

t = p.html(

    p.head(
        p.title('Sunflower Image')
    ),
    p.body(
        p.h1('This is Heading 1'),
        p.b('This text\n in bold')
    )
)

print(t.render())