viewstate = None
eventvalidation = None
viewstategenerator = None
data = {
    'ctl00_ToolkitScriptManager1_HiddenField': '',
    # 目前頁面，課程公告為0，課程檢索為1，已選課表為2。
    'ctl00_MainContent_TabContainer1_ClientState': '{"ActiveTabIndex":2,"TabState":[true,true,true]}',
    # 觸發此次請求的元素，按鈕或是連結。有以下幾種:
    #     課程檢索:
    #         依開課系所的查詢按鈕'ctl00$MainContent$TabContainer1$tabCourseSearch$wcCourseSearch$btnSearch'
    #         依輸入條件的查詢按鈕'ctl00$MainContent$TabContainer1$tabCourseSearch$wcCourseSearch$btnSearchOther'
    #         去選課的連結'ctl00$MainContent$TabContainer1$tabCourseSearch$wcCourseSearch$lbtnGoToSelectedTab'
    #         查詢結果的關注按鈕、查詢結果的取消按鈕''
    #     已選課表:
    #         選課查詢:
    #             選課代號的查詢按鈕''
    #             加選按鈕、未加選時登記人數按鈕'ctl00$MainContent$TabContainer1$tabSelected$gvToAdd'
    #             退選按鈕、已加選時登記人數按鈕'ctl00$MainContent$TabContainer1$tabSelected$gvToDel'
    #         關注清單: (從102開始往下加2)
    #             加選按鈕'ctl00$MainContent$TabContainer1$tabSelected$gvWishList$ctl02$btnAdd'
    #             登記人數按鈕'ctl00$MainContent$TabContainer1$tabSelected$gvWishList$ctl02$btnQuota'
    #             取消關注按鈕'ctl00$MainContent$TabContainer1$tabSelected$gvWishList$ctl02$btnRemoveItem'
    '__EVENTTARGET': 'ctl00$MainContent$TabContainer1$tabSelected$gvWishList$ctl04$btnAdd',
    # 附加資訊，告訴服務端如何處理事件。非關注清單的加選addCourse$0、退選delCourse$0、登記人數查詢selquota$0，其餘為空字串。
    '__EVENTARGUMENT': '',
    '__LASTFOCUS': '',
    # 0、1不影響。已選課表的查詢按鈕按第二次會設0、關注清單加選按鈕按第二次會設1，其餘不會改變值，所以1或0不影響。
    'ctl00_MainContent_TabContainer1_tabSelected_TabContainer2_ClientState': '{"ActiveTabIndex":0,"TabState":[true,true,true]}',
    # 目前網站的狀態或是資料。
    '__VIEWSTATE': viewstate,
    # 生成 __VIEWSTATE 的驗證碼。02808545、7CD65F6F...等等
    '__VIEWSTATEGENERATOR': viewstategenerator,
    # 加密的 __VIEWSTATE。
    '__VIEWSTATEENCRYPTED': '',
    # 用來驗證表單的有效性，確保用戶不會提交有效性不符合預期的表單。
    '__EVENTVALIDATION': eventvalidation,

    # 學制預設大學部1，碩士3、博士4、進修學士5，沒有2。
    'ctl00$MainContent$TabContainer1$tabCourseSearch$wcCourseSearch$ddlDegree': '1',
    # 學院有選就有字串，沒選就空字串。分別為AS建築、CA工科、CB商、CC創能、建設CD、金融CF、人社CH、資電CI、通識中心GE、國科管NM、學分學程PC、大學社會SX、外語XA、通識核心XC、體育XD、綜合XE、統籌XF、軍訓XH。
    'ctl00$MainContent$TabContainer1$tabCourseSearch$wcCourseSearch$ddlDept': '',
    # 系所預設全部空字串。
    'ctl00$MainContent$TabContainer1$tabCourseSearch$wcCourseSearch$ddlUnit': '',
    # 班級預設全部空字串。
    'ctl00$MainContent$TabContainer1$tabCourseSearch$wcCourseSearch$ddlClass': '',

    # 選課代號有勾就有這條。
    'ctl00$MainContent$TabContainer1$tabCourseSearch$wcCourseSearch$cbOtherCondition1': 'on',
    # 星期有勾就有這條。
    'ctl00$MainContent$TabContainer1$tabCourseSearch$wcCourseSearch$cbOtherCondition2': 'on',
    # 科目名稱有勾就有這條。
    'ctl00$MainContent$TabContainer1$tabCourseSearch$wcCourseSearch$cbOtherCondition3': 'on',
    # 開課老師姓名有勾就有這條。
    'ctl00$MainContent$TabContainer1$tabCourseSearch$wcCourseSearch$cbOtherCondition4': 'on',
    # 授課語言有勾就有這條。
    'ctl00$MainContent$TabContainer1$tabCourseSearch$wcCourseSearch$cbOtherCondition5': 'on',
    # 特定科目有勾就有這條。
    'ctl00$MainContent$TabContainer1$tabCourseSearch$wcCourseSearch$cbOtherCondition6': 'on',

    # 選課代號有填就有數字，沒填就空字串。
    'ctl00$MainContent$TabContainer1$tabCourseSearch$wcCourseSearch$tbSubID': '',
    # 星期有選就有數字，全選就空字串。
    'ctl00$MainContent$TabContainer1$tabCourseSearch$wcCourseSearch$ddlWeek': '',
    # 節次有選就有數字，全選就空字串。
    'ctl00$MainContent$TabContainer1$tabCourseSearch$wcCourseSearch$ddlPeriod': '',
    # 科目名稱有填就有字串，沒填就空字串。
    'ctl00$MainContent$TabContainer1$tabCourseSearch$wcCourseSearch$tbCourseName': '',
    # 開課老師姓名有填就有字串，沒填就空字串。
    'ctl00$MainContent$TabContainer1$tabCourseSearch$wcCourseSearch$tbTeacherName': '',
    # 授課語言預設中文01，01到08依序為中、英、日、德、法、西、其他、中英。
    'ctl00$MainContent$TabContainer1$tabCourseSearch$wcCourseSearch$ddlUseLanguage': '01',
    # 特定科目預設通識1。
    'ctl00$MainContent$TabContainer1$tabCourseSearch$wcCourseSearch$ddlSpecificSubjects': '1',



# 全部情況都有以下一條，而只有這一條的為已選課表頁的加選、退選、登記人數按鈕。
    # 是否顯示已選擇的課程，基本上都為on。
    'ctl00$MainContent$TabContainer1$tabCourseSearch$wcCourseSearch$cbShowSelected': 'on',
    
# 已選的通識志願序，102開始，後面都加1。
    'ctl00$MainContent$TabContainer1$tabSelected$TabContainer2$genSubTab$gvPerSelGe$ctl02$geDropDownList': '1',
    'ctl00$MainContent$TabContainer1$tabSelected$TabContainer2$genSubTab$gvPerSelGe$ctl03$geDropDownList': '2',


# 課程檢索頁的查詢按鈕，新增以下三條。
    # 查詢結果的第幾頁，有時候會算錯。第一頁可能不顯示這條或顯示1，後面頁算法:按左右有可能+1有可能-1有可能不變，下拉選直接指定值。
    # 'ctl00$MainContent$TabContainer1$tabCourseSearch$wcCourseSearch$ddlPageCurrent': '1',
    # 已選課表頁的選課代號，空字有填就有數字，沒填就空字串。
    'ctl00$MainContent$TabContainer1$tabSelected$tbSubID': '',
    # true、false不影響，只有已選課表頁的取消關注按鈕會主動設為false，其餘不會改變值，預設為true。
    'ctl00$MainContent$TabContainer1$tabSelected$cpeWishList_ClientState': 'true',
# 課程檢索頁的關注按鈕，新增以下三條。
    # 根據第幾個關注，從102開始加2
    'ctl00$MainContent$TabContainer1$tabCourseSearch$wcCourseSearch$gvSearchResult$ctl02$btnAdd': '關注',
    'ctl00$MainContent$TabContainer1$tabSelected$tbSubID': '',
    'ctl00$MainContent$TabContainer1$tabSelected$cpeWishList_ClientState': 'true',
# 課程檢索頁的關注按鈕，新增以下三條。
    # 根據關注的數字取消
    'ctl00$MainContent$TabContainer1$tabCourseSearch$wcCourseSearch$gvSearchResult$ctl02$btnRemove': '取消',
    'ctl00$MainContent$TabContainer1$tabSelected$tbSubID': '',
    'ctl00$MainContent$TabContainer1$tabSelected$cpeWishList_ClientState': 'true',
# 已選課表頁的查詢按鈕，新增以下三條。
    'ctl00$MainContent$TabContainer1$tabSelected$tbSubID': '',
    'ctl00$MainContent$TabContainer1$tabSelected$btnGetSub': '查詢',
    'ctl00$MainContent$TabContainer1$tabSelected$cpeWishList_ClientState': 'true',
# 已選課表頁的取消關注按鈕，新增以下兩條。
    'ctl00$MainContent$TabContainer1$tabSelected$tbSubID': '',
    'ctl00$MainContent$TabContainer1$tabSelected$cpeWishList_ClientState': 'false',
}