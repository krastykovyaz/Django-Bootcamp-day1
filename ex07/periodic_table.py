def form_table(elements):
    peaces_html = ''
    pos = 0
    for element, data in elements.items():
        cur_pos = int(data['position'])
        if cur_pos == 0:
            peaces_html += " <tr>\n"
        for i in range(cur_pos - pos):
            if i > 0:
                peaces_html += '''
                    <td style="border: 1px solid black; padding:10px"> 
                     
                    </td>
                    '''
        pos = cur_pos
        if cur_pos == 17:
            pos = 0
        elect = elements[element]['electron'].split()
        count_e = 0
        for e in elect:
            count_e += int(e)
        peaces_html += f'''
        <td style="border: 1px solid black; padding:10px"> <h4>{ element }</h4>
            <ul>
                <li>{ elements[element]['position'] }</li>
                <li><h2>{ elements[element]['small'] }</h2></li> 
                <li>Mass: { elements[element]['molar'] }</li>
                <li>Electrons: { count_e }</li>
            </ul>
        </td>
        '''
        if data['position'] == '17':
            peaces_html += " </tr>\n"
    return peaces_html


def gen_html(table_data):
    html_page = '''
    <!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <title>Mendeleev table</title>
</head>

<body>
<table>
    %s
    </table>
</body>    
</html>
    ''' % form_table(table_data)
    return html_page


def read_periodic_table():
    periodic_table = {}
    handle = open('periodic_table.txt', 'r')
    for line in handle:
        line = line.rstrip('\n')
        element = line.split('=')[0].strip()
        data = line.split('=')[1].strip()
        list_data = data.split(',')
        tmp_collector = {}
        for d in list_data:
            d = d.strip()
            d = d.split(':')
            tmp_collector[d[0].strip()] = d[1].strip()
        periodic_table[element] = tmp_collector
    html = gen_html(periodic_table)
    with open('periodic_table.html', 'w+') as handle:
        handle.write(html)


if __name__ == '__main__':
    read_periodic_table()