# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <codecell>

import xml.etree.ElementTree as etree
filename='LRG_292.xml'
which_annotation='fixed_annotation'

tree = etree.parse(filename)
schema=tree.getroot()
print schema.attrib

for annotation in schema:
    if annotation.tag==which_annotation:
        print annotation.tag #, annotation.attrib     
        ID=annotation.find('id').text
        print ID
        
        SEQ=annotation.find('sequence').text
       # print SEQ
        print "end of genomic seq"
        
        for transcript in annotation:
            if transcript.tag=='transcript':
                print transcript.tag, transcript.attrib
            
                for exon in transcript:
                    if exon.tag=='exon':                    
                        for coords in exon:
                            if (coords.attrib['coord_system']==str(ID)):                           
                                start=int(coords.attrib ['start'])
                                end=int(coords.attrib ['end'])
                                exon_seq=SEQ[start-1:end]
                                val_exon_seq_len=(end+1)-start
                                #diff_len=int(val_exon_seq_len)-int(exon_seq)                           
                                                         
                                print exon.tag, exon.attrib, start, end, exon_seq, val_exon_seq_len, len(exon_seq)
                                if (len(exon_seq)!=val_exon_seq_len):
                                    print "Problem validating exon_sequence length"
                        
        #ALLSEQ=annotation.findall('sequence')
        #print ALLSEQ

        #print annotation[0].text
        #print annotation[1].text
        print "End of annotation!"
        print '\n'
    



        

# <codecell>


