from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import time

class JobAdImporter:
    def __init__(self, url):
        self.url = url
        self.headers = {
            "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36"
            }
        self.driver = None
        self.soup = None

    def selenium_decorator(func):
        """
        Decorator to manage a Chrome WebDriver for data scraping.

        Args:
            func: The function to be decorated.

        Returns:
            A wrapper function that handles WebDriver setup and teardown.
        """
        def wrapper(self, *args, **kwargs):
            chrome_options = webdriver.ChromeOptions()
            chrome_options.add_experimental_option("detach", True)
            self.driver = webdriver.Chrome(options=chrome_options)
            try:
                self.driver.get(self.url)
                time.sleep(2)
                result = func(self, *args, **kwargs) # call the decorated function
                return result
            except Exception as e:
                print(f"Error during information retrieval: {e}")
            # finally:
            #     self.driver.quit()
        return wrapper
    
    def soup_decorator(func):
        """
        Decorator to manage a BeautifulSoup object for data scraping.

        Args:
            func: The function to be decorated.

        Returns:
            A wrapper function that handles BeautifulSoup setup and teardown.
        """
        def wrapper(self, *args, **kwargs):
            website = requests.get(self.url, headers=self.headers)
            try:
                self.soup = BeautifulSoup(website.text, "html.parser")
                result = func(self, *args, **kwargs) # call the decorated function
                return result
            except Exception as e:
                print(f"Error during information retrieval: {e}")
        return wrapper


    @selenium_decorator
    def get_indeed_information(self):
        """
        Retrieves job ad information from Indeed with Selenium, returns a dictionary.
        """

        # decline cookies
        cookies = self.driver.find_element(By.XPATH, '//*[@id="onetrust-reject-all-handler"]')
        cookies.click()
        print("Cookies declined")
        # get job title
        time.sleep(3)
        try:
            job_title = self.driver.find_element(By.XPATH, '//*[@id="jobsearch-ViewjobPaneWrapper"]/div/div/div/div[1]/div/div[2]/div[1]/h2/span')
            company_name = self.driver.find_element(By.XPATH, '//*[@id="jobsearch-ViewjobPaneWrapper"]/div/div/div/div[1]/div/div[2]/div[2]/div/div/div/div[1]/div[1]/span/a')
            company_location = self.driver.find_element(By.XPATH, '//*[@id="jobsearch-ViewjobPaneWrapper"]/div/div/div/div[1]/div/div[2]/div[2]/div/div/div/div[2]/div')
            job_description = self.driver.find_element(By.XPATH, '//*[@id="jobDescriptionText"]')
        except NoSuchElementException:
            print("Element not found")

        return {
            "job_title": job_title.text.replace("- job post", "").strip(),
            "company_name": company_name.text.strip(),
            "company_location": company_location.text.strip(),
            "job_description": job_description.text.replace("\n"," ").strip()
            }
        
    @soup_decorator
    def get_baito_information(self):
        """
        Retrieves job ad information from Baito with BeautifulSoup, returns a dictionary.
        """
        job_title = self.soup.find("span", {"data-br": ":R2r3brrqnlenla:"})
        company_name = self.soup.find("span", class_="font-bold text-primary")
        location_tag = self.soup.find("a", class_ ="ml-2")
        company_location = location_tag.div.next_element.next_element.next_element.next_element.text
        description_tag = self.soup.find("div", class_="jobDescription")
        job_description = description_tag.div.div.div.div

        return {
            "job_title": job_title.text.replace("Stellenausschreibung: ", "").strip(),
            "company_name": company_name.text.strip(),
            "company_location": company_location,
            "job_description": job_description.text.replace("\n"," ").strip()
            }

    @soup_decorator
    def get_personio_information(self):
        """
        Retrieves job ad information from Personio with BeautifulSoup, returns a dictionary.
        """
        title_tag = self.soup.title.text
        job_title = title_tag.split("|")[0].strip()
        company_name =  title_tag.split("|")[1].replace("Jobs at", "").strip()
        location_tag = self.soup.find("h6", class_ ="detail-subtitle")
        company_location = location_tag.span.span.text
        job_description = self.soup.find("article", class_="detail-content-block")

        return {
            "job_title": job_title,
            "company_name": company_name,
            "company_location": company_location,
            "job_description": job_description.text.replace("\n"," ").strip()
            }
        
    @soup_decorator
    def get_xing_information(self):
        """
        Retrieves job ad information from Xing with Beautiful Soup, returns a dictionary.
        """
        job_title = self.soup.find("h1", {"data-testid": "job-title"})
        company_name = self.soup.find("p", {"data-xds": "BodyCopy"})
        company_location = self.soup.find("li", {"data-testid": "location-info-icon"})
        job_description = self.soup.find("div", class_="section-content")

        return {
            "job_title": job_title.text.strip(),
            "company_name": company_name.text.strip(),
            "company_location": company_location.text.strip(),
            "job_description": job_description.text.replace("\n"," ").strip()
            }
        
    @soup_decorator
    def get_stepstone_information(self):
        """
        Retrieves job ad information from Stepstone with BeautifulSoup, returns a dictionary.
        """
        job_title = self.soup.find("span", class_="listing-content-provider-bewwo")
        company_name = self.soup.find("a", class_="listing-content-provider-zw6cpm")
        recruiter_name = self.soup.find("h3", class_="stst-css-yfbymk at-recruiter-name")
        recruiter_phone = self.soup.find("span", class_="stst-css-1jx3vjx")
        company_location = self.soup.find("span", class_="listing-content-provider-18c169z")
        company_info = self.soup.find("article", class_="listing-content-provider-1lx1y7n")
        tasks = self.soup.find("div", class_="listing-content-provider-15mhjzh at-section-text-description-content listingContentBrandingColor")
        profile = self.soup.find("div", class_="listing-content-provider-15mhjzh at-section-text-profile-content listingContentBrandingColor")
        job_description = tasks.text.replace("\n"," ").replace("\xa0","").strip() + " " + profile.text.replace("\n"," ").replace("\xa0","").strip()

        return {
            "job_title": job_title.text.strip(),
            "company_name": company_name.text.strip(),
            "recruiter_name": recruiter_name.text.strip(),
            "recruiter_phone": recruiter_phone.text.strip(),
            "company_location": company_location.text.strip(),
            "company_info": company_info.text.replace("\n"," ").replace("\xa0"," ").strip(),
            "job_description": job_description
            }
    
    @soup_decorator
    def get_monster_information(self):
        """
        Retrieves job ad information from monster with Beautiful Soup, returns a dictionary.
        """
        job_title = self.soup.find("h1", class_="headerstyle__JobViewHeaderTitle-sc-1ijq9nh-5")
        company_name = self.soup.find("h2", class_="headerstyle__JobViewHeaderCompany-sc-1ijq9nh-6 bfsVOy")
        company_location = self.soup.find("h3", class_="headerstyle__JobViewHeaderLocation-sc-1ijq9nh-4 guqMDF")
        job_description = self.soup.find("div", class_="descriptionstyles__DescriptionContainer-sc-13ve12b-0 iCEVUR")

        return {
            "job_title": job_title.text.strip(),
            "company_name": company_name.text.strip(),
            "company_location": company_location.text.strip(),
            "job_description": job_description.text.replace("\n"," ").strip()
            }

    @selenium_decorator
    def get_glassdoor_information(self):
        """
        Retrieves job ad information from Glassdoor with Selenium, returns a dictionary.
        """
        print("data retrieval running")
        # decline cookies
        cookies = self.driver.find_element(By.ID, 'onetrust-reject-all-handler')
        cookies.click()
        time.sleep(1)

        # find information
        job_title = self.driver.find_element(By.XPATH, '//*[@id="jd-job-title-1009121435295"]')
        company_name = self.soup.find("span", class_="EmployerProfile_employerName__8w0tV")
        #company_location = self.soup.find("div", class_="JobDetails_location__MbnUM")
        #job_description = self.soup.find("section", class_="JobDetails_jobDetailsSection__PJz1h")

        return {
            "job_title": job_title.text.strip(),
            #"company_name": company_name.text.strip(),
            #"company_location": company_location.text.strip(),
            #"job_description": job_description.text.replace("\n"," ").strip()
            }
  

    def get_getinit_information(self):
        pass

    def get_wearedevelopers_information(self):
        pass

    def get_goodjobs_information(self):
        pass

    @soup_decorator
    def get_linked_in_information(self):
        """
        Retrieves job ad information from LinkedIn with Beautiful Soup, returns a dictionary.
        """
        pass
        #job_title = self.soup.find("a", class_="topcard__link")
        
        #company_name = self.soup.find("p", {"data-xds": "BodyCopy"})
        #company_location = self.soup.find("li", {"data-testid": "location-info-icon"})
        #job_description = self.soup.find("div", class_="section-content")

        #return {
        #    "job_title": job_title,
            #"company_name": company_name.text.strip(),
            #"company_location": company_location.text.strip(),
            #"job_description": job_description.text.replace("\n"," ").strip()
            #}
    

if __name__ == "__main__":
    #indeed_ad = JobAdImporter('https://de.indeed.com/jobs?q=python&l=berlin&from=searchOnHP&advn=95263882141188&vjk=2fcd8a5b9ce55739')
    #information = indeed_ad.get_indeed_information()
    #print(information)
    
    #baito_ad = JobAdImporter('https://www.getbaito.com/de/job/stellenausschreibung-mitarbeiterin-controlling-atze-musiktheater-atze-musiktheater-gmbh?location=berlin#topOfDescription')
    #information = baito_ad.get_baito_information()
    #print(information)

    #personio_ad = JobAdImporter('https://coffeecircle.jobs.personio.de/job/1417205?language=en&display=de')
    #information = personio_ad.get_personio_information()
    #print(information)

    # xing_ad = JobAdImporter('https://www.xing.com/jobs/berlin-python-engineer-116006448?paging_context=search&search_query%5Bkeywords%5D=python&search_query%5Blocation%5D=berlin&search_query%5Blimit%5D=20&search_query%5Boffset%5D=0&search_query%5Bpage%5D=1&ijt=jb_18')
    # information = xing_ad.get_xing_information()
    # print(information)

    # stepstone_ad = JobAdImporter('https://www.stepstone.de/stellenangebote--Softwareentwickler-in-Python-Berlin-aconium-GmbH--10565228-inline.html?rltr=3_3_25_seorl_m_0_0_0_0_1_0')
    # information = stepstone_ad.get_stepstone_information()
    # print(information)

    # monster_ad = JobAdImporter('https://www.monster.de/stellenangebot/python-entwickler-m-w-d-saas-berlin-16--3ac73924-ac92-437a-a22f-5e2f7689b1dc?sid=b7a8032c-4ca9-40e2-b0c7-74f7cd59c490&jvo=m.l.s-svr.5&so=m.h.s&hidesmr=1&promoted=LEXEME_PAID')
    # information = monster_ad.get_monster_information()
    # print(information)

    glassdoor_ad = JobAdImporter('https://www.glassdoor.de/job-listing/administrator-in-f%C3%BCr-san-storage-backup-it-dienstleistungszentrum-berlin-JV_IC2622109_KO0,39_KE40,72.htm?jl=1009121435295&cs=1_a005aa61&s=58&t=SR&pos=102&src=GD_JOB_AD&cpc=0215C0D262B7DA96&guid=0000018db22c37aca7ef5c95edbeb4ce&jobListingId=1009121435295&ao=1110586&vt=w&jrtk=5-yul1-0-1hmp2odv2k5re800-56db813e1e9f5716---6NYlbfkN0Aa6v4DJDDz3707DdH_z5HkGRL_fL-_0NbcjDba1pJn8O3E5Rb90OmkMzgfJGAXE7wIyZfWCoySQ4Zj9xAVsA3dwW7r58b3TUHYdiN8k-toRWFzIj7eVCoNckEKwHBzqqKP4PTcjPFquQAkXFsx1-_eRz3QumKPrqoTtc-YFOBuF23pPZzbqqpqmelrIu8mcfyK84YYCD82KljRam49qKS0zBdrnzjyTsaWvBjeZmK-21wXzVEe2kcnwuicS4KwkeO_m72iT8JgEhMh5RtHL61TGAMkZT2dnoQzRvb0IFrsncJ-zDtISf2HUOC2wBrhlTPzv5wsh5m19oebz1ywqaGRifrOqqUap2TG8B-BhlpNBuYUDGr2MoA8-c_W7zFJDAbPBqAtKlAojXQfZrhAsA8V_gDuMvvNqPmPcSktOoihMit3o6dxoLJjQ8xwkiQgz8yh24Gzu3Ch-lisi8Q7GiwbpHDUW6einP-4L3ymUru2h0lHyIwg4hzuAnzmH5s2wpCFzzzpdn72Q3e3Si6SHNTwo8kzgyB51Ad_BoVVf_mb8tdzqnE10MD1W2TtN9250a92_DhZZpPyNHSizq9DRsd0UHxwKacVLuGIngc639gGNn6U8BK8IDbL3UQxexUDDo8SiqJABb44OnTtJ214h_uNngjmHoFkftKXkC_Qd2pu-z3OEUg1Yr8y&cb=1708091259120&ctt=1708091270694')
    information = glassdoor_ad.get_glassdoor_information()
    print(information)