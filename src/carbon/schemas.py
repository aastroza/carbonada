from enum import Enum
from pydantic import BaseModel, Field

class ProductDatasetEntry(BaseModel):
    product: str
    carbon_footprint: float
    source: str

class IndustryDatasetEntry(BaseModel):
    industry: str
    country: str
    carbon_footprint_per_USD: float
    source: str

class Industry(str, Enum):
    crop_and_animal_production_hunting_and_related_service_activities = "Crop And Animal Production, Hunting And Related Service Activities"
    forestry_and_logging = "Forestry And Logging"
    fishing_and_aquaculture = "Fishing And Aquaculture"
    mining_of_coal_and_lignite = "Mining Of Coal And Lignite"
    extraction_of_crude_petroleum_and_natural_gas_mining_of_metal_ores = "Extraction Of Crude Petroleum And Natural Gas & Mining Of Metal Ores"
    other_mining_and_quarrying = "Other Mining And Quarrying"
    mining_support_service_activities = "Mining Support Service Activities"
    processing_and_preserving_of_meat_and_production_of_meat_products = "Processing and preserving of meat and production of meat products"
    processing_and_preserving_of_fish_crustaceans_molluscs_fruit_and_vegetables = "Processing and preserving of fish, crustaceans, molluscs, fruit and vegetables"
    manufacture_of_vegetable_and_animal_oils_and_fats = "Manufacture of vegetable and animal oils and fats"
    manufacture_of_dairy_products = "Manufacture of dairy products"
    manufacture_of_grain_mill_products_starches_and_starch_products = "Manufacture of grain mill products, starches and starch products"
    manufacture_of_bakery_and_farinaceous_products = "Manufacture of bakery and farinaceous products"
    manufacture_of_other_food_products = "Manufacture of other food products"
    manufacture_of_prepared_animal_feeds = "Manufacture of prepared animal feeds"
    manufacture_of_alcoholic_beverages_tobacco_products = "Manufacture of alcoholic beverages  & Tobacco Products"
    manufacture_of_soft_drinks_production_of_mineral_waters_and_other_bottled_waters = "Manufacture of soft drinks; production of mineral waters and other bottled waters"
    manufacture_of_textiles = "Manufacture Of Textiles"
    manufacture_of_wearing_apparel = "Manufacture Of Wearing Apparel"
    manufacture_of_leather_and_related_products = "Manufacture Of Leather And Related Products"
    manufacture_of_wood_products_of_wood_cork_except_furniture_manuf_of_articles_of_straw = "Manufacture Of Wood & Products Of Wood & Cork, Except Furniture; Manuf. Of Articles Of Straw"
    manufacture_of_paper_and_paper_products = "Manufacture Of Paper And Paper Products"
    printing_and_reproduction_of_recorded_media = "Printing And Reproduction Of Recorded Media"
    manufacture_of_coke_and_refined_petroleum_products = "Manufacture Of Coke And Refined Petroleum Products"
    manufacture_of_paints_varnishes_and_similar_coatings_printing_ink_and_mastics = "Manufacture of paints, varnishes and similar coatings, printing ink and mastics"
    manufacture_of_soap_detergents_cleaning_polishing_perfumes_toilet_preparations = "Manufacture of soap & detergents, cleaning & polishing, perfumes & toilet preparations"
    manufacture_of_other_chemical_products = "Manufacture of other chemical products"
    manufacture_of_industrial_gases_inorganics_and_fertilisers_inorganic_chemicals_20_11_13_15 = "Manufacture of industrial gases, inorganics and fertilisers (inorganic chemicals) - 20.11/13/15"
    manufacture_of_petrochemicals_20_14_16_17_60 = "Manufacture of petrochemicals - 20.14/16/17/60"
    manufacture_of_dyestuffs_agro_chemicals_20_12_20 = "Manufacture of dyestuffs, agro-chemicals - 20.12/20"
    manufacture_of_basic_pharmaceutical_products_and_pharmaceutical_preparations = "Manufacture Of Basic Pharmaceutical Products And Pharmaceutical Preparations"
    manufacture_of_rubber_and_plastic_products = "Manufacture Of Rubber And Plastic Products"
    manufacture_of_cement_lime_plaster_and_articles_of_concrete_cement_and_plaster = "Manufacture of cement, lime, plaster and articles of concrete, cement and plaster"
    manufacture_of_glass_refractory_clay_porcelain_ceramic_stone_products_23_1_4_7_9 = "Manufacture of glass, refractory, clay, porcelain, ceramic, stone products - 23.1-4/7-9"
    manufacture_of_basic_iron_and_steel = "Manufacture of basic iron and steel"
    manufacture_of_other_basic_metals_and_casting = "Manufacture of other basic metals and casting"
    manufacture_of_weapons_and_ammunition = "Manufacture of weapons and ammunition"
    manufacture_of_fabricated_metal_products_excluding_weapons_ammunition_25_1_3_5_9 = "Manufacture of fabricated metal products, excluding weapons & ammunition - 25.1-3/5-9"
    manufacture_of_computer_electronic_and_optical_products = "Manufacture Of Computer, Electronic And Optical Products"
    manufacture_of_electrical_equipment = "Manufacture Of Electrical Equipment"
    manufacture_of_machinery_and_equipment_n_e_c = "Manufacture Of Machinery And Equipment N.E.C."
    manufacture_of_motor_vehicles_trailers_and_semi_trailers = "Manufacture Of Motor Vehicles, Trailers And Semi-Trailers"
    building_of_ships_and_boats = "Building of ships and boats"
    manufacture_of_air_and_spacecraft_and_related_machinery = "Manufacture of air and spacecraft and related machinery"
    manufacture_of_other_transport_equipment_30_2_4_9 = "Manufacture of other transport equipment - 30.2/4/9"
    manufacture_of_furniture = "Manufacture Of Furniture"
    other_manufacturing = "Other Manufacturing"
    repair_and_maintenance_of_ships_and_boats = "Repair and maintenance of ships and boats"
    repair_and_maintenance_of_aircraft_and_spacecraft = "Repair and maintenance of aircraft and spacecraft"
    rest_of_repair_installation_33_11_14_17_19_20 = "Rest of repair; Installation - 33.11-14/17/19/20"
    electric_power_generation_transmission_and_distribution = "Electric power generation, transmission and distribution"
    manufacture_of_gas_distribution_of_gaseous_fuels_through_mains_steam_and_aircon_supply = "Manufacture of gas; distribution of gaseous fuels through mains; steam and aircon supply"
    water_collection_treatment_and_supply = "Water Collection, Treatment And Supply"
    sewerage = "Sewerage"
    waste_collection_treatment_and_disposal_activities_materials_recovery = "Waste Collection, Treatment And Disposal Activities; Materials Recovery"
    remediation_activities_and_other_waste_management_services = "Remediation Activities And Other Waste Management Services"
    construction = "Construction"
    wholesale_and_retail_trade_and_repair_of_motor_vehicles_and_motorcycles = "Wholesale And Retail Trade And Repair Of Motor Vehicles And Motorcycles"
    rail_transport = "Rail transport"
    land_transport_services_and_transport_services_via_pipelines_excluding_rail_transport = "Land transport services and transport services via pipelines, excluding rail transport"
    water_transport = "Water Transport"
    air_transport = "Air Transport"
    warehousing_and_support_activities_for_transportation = "Warehousing And Support Activities For Transportation"
    postal_and_courier_activities = "Postal And Courier Activities"
    accommodation = "Accommodation"
    food_and_beverage_service_activities = "Food And Beverage Service Activities"
    publishing_activities = "Publishing Activities"
    motion_picture_video_tv_programme_production_sound_recording_music_publishing_activities_programming_and_broadcasting_activities = "Motion Picture, Video & TV Programme Production, Sound Recording & Music Publishing Activities & Programming And Broadcasting Activities"
    telecommunications = "Telecommunications"
    computer_programming_consultancy_and_related_activities = "Computer Programming, Consultancy And Related Activities"
    information_service_activities = "Information Service Activities"
    financial_service_activities_except_insurance_and_pension_funding = "Financial Service Activities, Except Insurance And Pension Funding"
    insurance_and_reinsurance_except_compulsory_social_security_pension_funding = "Insurance and reinsurance, except compulsory social security & Pension funding"
    activities_auxiliary_to_financial_services_and_insurance_activities = "Activities Auxiliary To Financial Services And Insurance Activities"
    buying_and_selling_renting_and_operating_of_own_or_leased_real_estate_excluding_imputed_rent = "Buying and selling, renting and operating of own or leased real estate, excluding imputed rent"
    owner_occupiers_housing = "Owner-Occupiers' Housing"
    real_estate_activities_on_a_fee_or_contract_basis = "Real estate activities on a fee or contract basis"
    legal_activities = "Legal activities"
    accounting_bookkeeping_and_auditing_activities_tax_consultancy = "Accounting, bookkeeping and auditing activities; tax consultancy"
    activities_of_head_offices_management_consultancy_activities = "Activities Of Head Offices; Management Consultancy Activities"
    architectural_and_engineering_activities_technical_testing_and_analysis = "Architectural And Engineering Activities; Technical Testing And Analysis"
    scientific_research_and_development = "Scientific Research And Development"
    advertising_and_market_research = "Advertising And Market Research"
    other_professional_scientific_and_technical_activities = "Other Professional, Scientific And Technical Activities"
    veterinary_activities = "Veterinary Activities"
    rental_and_leasing_activities = "Rental And Leasing Activities"
    employment_activities = "Employment Activities"
    travel_agency_tour_operator_and_other_reservation_service_and_related_activities = "Travel Agency, Tour Operator And Other Reservation Service And Related Activities"
    security_and_investigation_activities = "Security And Investigation Activities"
    services_to_buildings_and_landscape_activities = "Services To Buildings And Landscape Activities"
    office_administrative_office_support_and_other_business_support_activities = "Office Administrative, Office Support And Other Business Support Activities"
    public_administration_and_defence_compulsory_social_security = "Public Administration And Defence; Compulsory Social Security"
    education = "Education"
    human_health_activities = "Human Health Activities"
    residential_care_social_work_activities = "Residential Care  & Social Work Activities"
    creative_arts_and_entertainment_activities = "Creative, Arts And Entertainment Activities"
    libraries_archives_museums_and_other_cultural_activities = "Libraries, Archives, Museums And Other Cultural Activities"
    gambling_and_betting_activities = "Gambling And Betting Activities"
    sports_activities_and_amusement_and_recreation_activities = "Sports Activities And Amusement And Recreation Activities"
    activities_of_membership_organisations = "Activities Of Membership Organisations"
    repair_of_computers_and_personal_and_household_goods = "Repair Of Computers And Personal And Household Goods"
    other_personal_service_activities = "Other Personal Service Activities"
    activities_of_households_as_employers_of_domestic_personnel = "Activities Of Households As Employers Of Domestic Personnel"


class Query(BaseModel):
    industry: Industry
    cost_reasoning: str = Field(..., description="Reasoning behind the estimated cost of the product/service in USD")
    cost: float = Field(..., description="Estimated cost of the product/service in USD")

class Estimation(BaseModel):
    product: str
    industry: str
    carbon_footprint: float
    carbon_footprint_per_USD: float
    country: str
    cost: float
    cost_reasoning: str
    source: str
    model: str