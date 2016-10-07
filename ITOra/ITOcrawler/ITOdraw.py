#!coding = utf-8
import matplotlib.pyplot as plt
import numpy as np
import compstats
from matplotlib.font_manager import FontProperties
#ls $PWD/'Hiragino Sans GB W6.otf'
zhfont1 = FontProperties(fname = '/home/Jkob/Github/Mysqlex/ITOra/ITOcrawler/Hiragino Sans GB W6.otf')

company_stats = compstats.get_stats()
def drawbarhist(items_list):
        content=items_list[0]
        stats = items_list[1]        
        y_axis = np.arange(1,len(content)+1,1)

        plt.barh(y_axis,stats,align='center',color='#fd6854')
        plt.yticks(y_axis,content,fontproperties=zhfont1)
        plt.show()


drawbarhist(company_stats[0])
drawbarhist(company_stats[1])
drawbarhist(company_stats[2])
drawbarhist(company_stats[3])


