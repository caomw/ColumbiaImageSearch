import happybase

if __name__=="__main__":
    tab_image = 'escorts_images_similar_row'    
    conn = happybase.Connection(host='10.1.94.57')
    image_sha1s = '1000013C0A38D8DACAEC31360AFAFEB5DC3D712B'
    table = conn.table(tab_image)
    row = table.row(image_sha1s,columns=['s'])
    print len(row.keys()),[x.split(':')[-1] for x in row.keys()]
