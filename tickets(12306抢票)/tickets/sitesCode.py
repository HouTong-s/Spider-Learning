#站点处理类
class SitesCode:
    def __init__(self):
        self._sites = {}                           #存储站点名和站点编码的字典
        self.get_sites_from_file()             #从文件中获取站点信息

    #从文件中获取站点信息（站点名和站点编码）
    def get_sites_from_file(self):
        with open("sites.txt", "r", encoding="utf-8") as f:
            for site in f:
                site = site.strip("\n").split(":")
                                                #清除换行符并获取站点名和站点编码
                site_name = site[0]             #站点名
                site_code = site[1]             #站点编码
                self._sites[site_name] = site_code

    #判断站点名是否存在
    def is_exist(self, site_name):
        if site_name not in self._sites:
            return False                          #站点名不存在
        return True                                #站点名存在

    #根据站点名获取编码
    def name_2_code(self, site_name):
        return self._sites[site_name]