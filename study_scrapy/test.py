print(str(' 东源县革命老区发展史/全国革命老区县发展').replace('/', '-'))

insert_sql = '''
INSERT INTO book(name, src) values ("{}","{}")
'''.format('name', 'src')

print(insert_sql)