
class Urls:
    """web urls"""
    BASE_URL = "https://rconline.bihar.gov.in/rcmsadmin/(S(3cadwqrsaomyu22vbaz5p1aa))/RCIssueSystem/RCIssueLogin.aspx"
    #MO_FIELD_VERIFICATION = "https://rconline.bihar.gov.in/rcmsadmin/(S(3cadwqrsaomyu22vbaz5p1aa))/RCIssueSystem/RCIssueLogin.aspx"     

class Attributes:
    """Html tags attributes"""
    USERNAME_ID = "ContentPlaceHolder2_TxtUid"
    PASSWORD_ID = "ContentPlaceHolder2_TxtPwd"
    LOGIN_BUTTON_NAME = "ctl00$ContentPlaceHolder2$BtnLogin"
    OTP_LOGIN_BUTTON_NAME = ""
    OTP_LOGIN_BUTTON_ID = "ContentPlaceHolder2_btnOTPSubmit"
    #MO_FIELD_VERIFICATION = '//*[@id="smoothmenu1"]/ul/li[2]/a'
    FIELD_VERIFICATION_BUTTON = '//*[@id="smoothmenu1"]/ul/li[2]/ul/li[1]/ul/li[1]/a' 
    RURAL_RADIO_BUTTON = "ContentPlaceHolder2_radArea_0"
    APPLICATION_ID_CHECKBOX = "ContentPlaceHolder2_UCRuralFilter_chkAppid"
    FIELD_VERIFICATION_NAME = "ContentPlaceHolder2_txtFieldVerificatioBy"
    DESIGNATION_NAME = "ContentPlaceHolder2_txtDesignation"
    VERIFICATION_DATE = "ContentPlaceHolder2_txtDate"
    DISTRIC_NAME = "ctl00$ContentPlaceHolder1$ddldistrict"
    SUBDIVISION_NAME = "ctl00$ContentPlaceHolder1$ddlsubdivision"
    BLOCK_TOWN_NAME = "ctl00$ContentPlaceHolder1$ddlBlockTown"
    RC_NUMBER = "ContentPlaceHolder1_txtrcnumber"
    APPLICATION_ID = "ContentPlaceHolder2_UCRuralFilter_txtApplicationId"
    SHOW_REPORT = "ContentPlaceHolder2_btnShowRpt"
    SEARCH_BUTTON_ID = "ContentPlaceHolder1_btnsearch"
    VIEW_BUTTON = '//*[@id="ContentPlaceHolder2_gridview_member"]/tbody/tr[2]/td[12]' #Extract XPath of VIEW click

    # This might change in future
    MEMBER_LINK_XPATH = '//*[@id="ContentPlaceHolder2_gridview_member"]/tbody/tr[2]/td[12]'
    TABLE_ID = "ContentPlaceHolder2_gridview_member"
    ROW_XPATH = ".//tr" 
    DATA_XPATH = ".//td"
    #CHECK_BOX_ID = "gridview_member_chkSelect_[INDEX]"
    #NOTICE_ISSUE_NUMBER = "txtnoticeissueno"
    #ORDER_ISSUE_NUMBER = "txtorderissueno"
    #NOTICE_ISSUE_DATE = "txtnotieissuedate"
    #ORDER_ISSUE_DATE = "txtorderissuedate"
    #SOURCE_OF_INFO_DELETION = "ddlsourceofdeletion"
    #REASON_FOR_DELETON = "ddldelitionregion"
    #CHOOSE_FILE = "ContentPlaceHolder2_fluFieldVerificationFile"
    #ORDER_UPLOAD = "fileOrder"
    #FINAL_SUBMIT = "btnUpload"
    #MO_NAME = "txtmo"

    # Process of uploading file 
    CHOOSE_FILE = "ContentPlaceHolder2_fluFieldVerificationFile"
    UPDATE = "ContentPlaceHolder2_btnSubmit"

    # Applicant Field Verification Yes/No, For Yes INPUT BY NAME
    CHECK_BOX_YES_0 = "ContentPlaceHolder2_gridview_member_radList_0_0_0"
    CHECK_BOX_YES_NAME = "ctl00$ContentPlaceHolder2$gridview_member$ctl02$hdnMemberCode"
    CHECK_BOX_YES_0 = "ContentPlaceHolder2_gridview_member_radList_1_0_1"

    # SELECTION OF LIST OF YES = 0/NO = 1 OF ELEVEN COLUMNS
    TABLE_ID_VEHICLE_1 = "ContentPlaceHolder2_rad_Axn_R_IsVechile_1"
    TABLE_ID_MACHINE_2 = "ContentPlaceHolder2_rad_Axn_R_IsArgMachine_1"
    TABLE_ID_REG_3 = "ContentPlaceHolder2_rad_Axn_R_IsNonArgProfReg_1"
    TABLE_ID_INCOME_4 = "ContentPlaceHolder2_rad_Axn_R_IsFillMonthlyIncome_1"
    TABLE_ID_PAYTAX_5 = "ContentPlaceHolder2_rad_R_Axn_IsPayTax_1"
    TABLE_ID_PAYPROFTAX_6 = "ContentPlaceHolder2_rad_R_Axn_IsPayProfTax_1"
    TABLE_ID_WALLANDROOF_7 = "ContentPlaceHolder2_rad_R_Axn_IsWallAndRoof_1"
    TABLE_ID_ARGEQP_8 = "ContentPlaceHolder2_rad_R_Axn_R_IsArgEqp_1"
    TABLE_ID_CROPLAND_9 = "ContentPlaceHolder2_rad_R_Axn_R_IsHHCrp_1"
    TABLE_ID_ONEARC_FARMINGLAND_10 = "ContentPlaceHolder2_rad_R_Axn_R_IsOneArgEqp_1"
    TABLE_ID_GOVT_SERVICE_11 = "ContentPlaceHolder2_rad_R_Axn_IsFmlyService_1"

    # AFTER CLICKING ON NO TO ALL COLUMNS REMARKS TO BE WRITEDOWN
    REMARKS = "ContentPlaceHolder2_txtRemarks"

    # STATUS TO BE SELECTED 
    STATUS = "ContentPlaceHolder2_ddlStatus"
    VALUE_FOR_FIT_TO_BE_SELECTED = "Y"
    VALUE_FOR_FIT_TO_BE_REJECTED = "N"
    # SUBMIT TO FORWARD FOR AADHAR VERIFICATION
    SUBMIT_BUTTON_FORWARD_AADHAR_VERIFICATION = "ContentPlaceHolder2_btnUIDForward"

    # AADHAR VERIFICATION DETAILS PROCESS TO CLICK ON VERIFY BUTTON 
    # FIRST ROW NAMED WITH TABLE/COLUMN OF SL/NAME/AADHAR/VERIFY/IS AADHAR FOUND
    TABLE_ID_COLUMN_MEMBER_DETAILS = "ContentPlaceHolder2_pnlholdememberdetails"
    TABLE_GRID_VIEW_MEMBER = "ContentPlaceHolder2_gridview_member"
    SCOPE = "col" 
    ONCLICK ="OnOperate('S');"
    REMARKS_AADHAR_VERIFICATION = "ContentPlaceHolder2_txtRemarks"
    FINAL_ACCEPT_BUTTON = "ContentPlaceHolder2_btnAccept"


class Constants:
    "literal constants"
    INDEX = "[INDEX]"
    USERNAME = "USERNAME"
    PASSWORD = "PASSWORD"
    ENV = "ENV"
    APPLICATION_ID_NUM = 'Application Id Number'
    #NOTICE_NUM = 'Notice No'
    #NOTICE_DATE = 'Notice Date'
    #ORDER_NO = 'Order No'
    #ORDER_DATE = 'Order date'
