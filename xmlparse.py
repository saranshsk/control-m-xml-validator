import xml.etree.ElementTree as eT
try:
    import xml.etree.cElementTree as ET
except ImportError:
    import xml.etree.ElementTree as ET


tree = ET.ElementTree(file='test_xml.xml')
root = tree.getroot()
print root[0][0]
folder = root.get('FOLDER')
print(folder)

i = 0
jobs = {}
for job in root.iter('JOB'):
    try:
        key = job.tag + str(i)
        jobs[key] = job.attrib

        shout_list=[]
        for data in job.findall('.//SHOUT'):
            shout_list.append(data.attrib)
            jobs[key]["SHOUT"] = shout_list

        incond_list = []
        for data in job.findall('.//INCOND'):
            incond_list.append(data.attrib)
            jobs[key]["INCOND"] = incond_list

        outcond_list = []

        for data in job.findall('.//OUTCOND'):
            outcond_list.append(data.attrib)
            jobs[key]["OUTCOND"] = outcond_list
        i += 1
    except Exception as e:
        print e
print len(jobs)
print jobs['JOB0']
for key, value in jobs.items():
    print key
    print value
