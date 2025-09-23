from __future__ import annotations

import re
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[1]
CONTENT_DIR = BASE_DIR / "content" / "locations"
CONTENT_DIR.mkdir(parents=True, exist_ok=True)

IMAGE_PATH = "/images/hero-cloud.svg"


def slugify(name: str) -> str:
    slug = re.sub(r"[^a-z0-9]+", "-", name.lower())
    slug = slug.strip("-")
    return slug


region_descriptions = {
    "tweed-region": "across the Tweed Shire",
    "tweed-valley": "throughout the Tweed Valley",
    "tweed-heads": "around the Tweed Heads border region",
    "tweed-coast": "along the Tweed Coast",
    "tweed-river": "through the river villages of the Tweed",
    "tweed-hinterland": "through the Tweed hinterland",
    "tweed-forests": "in the forested foothills of Wollumbin",
    "tweed-rural": "across the rural communities of the Tweed",
    "gold-coast-coastal": "through the southern Gold Coast",
    "gold-coast-hinterland": "within the Gold Coast hinterland",
    "gold-coast-suburb": "around the southern Gold Coast suburbs",
}

area_closing = {
    "tweed-region": "We collaborate with councils, developers, and tourism operators right across the Tweed Shire, so it is easy to extend your support footprint to neighbouring communities when you work with us.",
    "tweed-valley": "Our technicians regularly travel the Tweed Valley, supporting clients from Murwillumbah to the surrounding villages, making onsite visits straightforward when you need them.",
    "tweed-heads": "Being based on the border means we are only minutes away from Tweed Heads, Banora Point, and the adjoining Queensland suburbs for rapid response.",
    "tweed-coast": "We spend much of our week on the Tweed Coast keeping resorts, retailers, and allied health practices connected from Kingscliff to Pottsville.",
    "tweed-river": "River communities rely on resilient systems, and we support businesses from Chinderah and Tumbulgum through to the cane farms inland.",
    "tweed-hinterland": "Creative studios, wellness retreats, and eco-tourism operators across the hinterland count on us for a mix of remote monitoring and timely onsite visits.",
    "tweed-forests": "With clients dotted around Wollumbin and the surrounding national park, we understand how to keep remote operations online and secure.",
    "tweed-rural": "From family farms to boutique producers, we help rural businesses link their sheds, offices, and field teams with dependable networks.",
    "gold-coast-coastal": "Our border location lets us respond quickly along the southern Gold Coast strip, from Coolangatta up to Burleigh and beyond.",
    "gold-coast-hinterland": "We work closely with hinterland retreats and acreage properties, designing technology that stands up to patchy infrastructure and seasonal tourism swings.",
    "gold-coast-suburb": "Being local to the southern Gold Coast means we can meet onsite fast while still delivering enterprise-grade remote monitoring and cloud expertise.",
}

type_service_paragraphs = {
    "region": "Tweed Cloud partners with councils, community organisations, developers, and established enterprises to deliver managed IT, cloud strategy, and cybersecurity leadership. Our border-based team understands the compliance expectations for both New South Wales and Queensland operations.",
    "major_town": "Tweed Cloud supports professional services, retail, healthcare, and community organisations in {name} with managed IT support, secure cloud migrations, and rapid onsite assistance. We design systems that keep staff productive across offices, shopfronts, and mobile teams.",
    "industrial": "Manufacturers, logistics depots, and trades working out of {name} rely on Tweed Cloud for rugged networks, cloud-based collaboration, and proactive monitoring. We help teams meet safety and compliance requirements without slowing down production.",
    "suburban": "Service businesses, clinics, and trades in {name} count on Tweed Cloud to keep devices, business apps, and communications platforms running smoothly. Our managed plans blend help desk responsiveness with strategic planning.",
    "coastal_village": "Hospitality venues, holiday rentals, and marine operators in {name} work with Tweed Cloud for resilient Wi-Fi, cloud-based booking systems, and security controls that protect guest data all season long.",
    "coastal_suburb": "From cafes and boutiques to allied health and tourism providers, businesses in {name} trust Tweed Cloud for fast connectivity, secure cloud collaboration, and a local help desk that understands coastal infrastructure challenges.",
    "river_village": "{name}'s riverfront businesses turn to Tweed Cloud for point-of-sale reliability, remote monitoring, and cyber security tuned for operators who balance tourism with essential services.",
    "hinterland_village": "Artisans, hospitality operators, and wellness retreats in {name} lean on Tweed Cloud to stabilise connectivity, modernise booking systems, and protect customer information across dispersed properties.",
    "rural_locality": "Farms, home-based studios, and contractors in {name} choose Tweed Cloud for dependable connectivity, cloud backups, and device security that works even when infrastructure is limited.",
    "growth_area": "Developers, builders, and service operators in {name} work with Tweed Cloud to deploy scalable connectivity, site security, and collaboration tools that keep new communities moving.",
    "gold_coast_coastal": "Tourism operators, wellness brands, and retail teams in {name} rely on Tweed Cloud for high-performing Wi-Fi, secure cloud applications, and a help desk that understands cross-border compliance.",
    "gold_coast_suburb": "Professional services, real estate agencies, and education providers in {name} engage Tweed Cloud for managed IT support, modern workplace collaboration, and layered cyber security defences.",
    "gold_coast_hinterland": "Retreats, acreage properties, and agribusinesses in {name} partner with Tweed Cloud to stabilise connectivity, deploy cloud-based workflows, and safeguard sensitive guest data.",
}

type_bullets = {
    "region": [
        "Strategic IT roadmaps that align councils and community programs",
        "Cloud migrations and Microsoft 365 governance across multi-site teams",
        "Cyber security frameworks that satisfy NSW and QLD requirements",
    ],
    "major_town": [
        "Managed service plans with proactive monitoring and help desk support",
        "Microsoft 365 and Google Workspace optimisation for hybrid teams",
        "Business continuity planning with secure cloud backups",
    ],
    "industrial": [
        "Rugged network design for warehouses and workshops",
        "Secure remote access for field crews and contractors",
        "Asset monitoring and alerting tied into production systems",
    ],
    "suburban": [
        "Device management and patching for growing service teams",
        "Secure VoIP and unified communications deployment",
        "Cyber awareness training tailored to local staff",
    ],
    "coastal_village": [
        "High-capacity Wi-Fi and mesh networks for guest areas",
        "Point-of-sale and booking platform integration",
        "Cyber security for hospitality teams handling card payments",
    ],
    "coastal_suburb": [
        "Network resilience for beachfront businesses and home offices",
        "Cloud collaboration platforms for multi-site teams",
        "Email security and backup to protect client data",
    ],
    "river_village": [
        "Failover connectivity to keep riverfront venues online",
        "Secure payment and reservation systems",
        "Proactive monitoring to minimise downtime during peak periods",
    ],
    "hinterland_village": [
        "Connectivity solutions that bridge studios, cabins, and farm stays",
        "Cloud-based booking and property management integrations",
        "Endpoint security that protects remote point-of-sale devices",
    ],
    "rural_locality": [
        "NBN, 4G, and satellite failover solutions",
        "Secure file sharing for contractors and consultants",
        "Automated backups that protect design and financial records",
    ],
    "growth_area": [
        "Temporary site connectivity for construction compounds",
        "Security camera and access control integrations",
        "Cloud reporting that keeps project stakeholders aligned",
    ],
    "gold_coast_coastal": [
        "Guest Wi-Fi and captive portal solutions for beachfront venues",
        "Managed point-of-sale and reservation platforms",
        "Cyber security and compliance support for tourism operators",
    ],
    "gold_coast_suburb": [
        "Modern workplace platforms with single sign-on and MFA",
        "Help desk coverage for distributed and remote staff",
        "Data protection and compliance reporting for regulated industries",
    ],
    "gold_coast_hinterland": [
        "Connectivity upgrades that handle acreage distances",
        "Cloud property management systems for retreats and farm stays",
        "Security awareness and policy development for seasonal teams",
    ],
}

locations = [
    {
        "name": "Tweed Shire",
        "state": "NSW",
        "area": "tweed-region",
        "type": "region",
        "intro": "The Tweed Shire brings together coastal villages, productive farmland, and rainforest communities along the NSW and Queensland border. Its growing population depends on resilient infrastructure to serve tourism, agriculture, education, and government services.",
    },
    {
        "name": "Murwillumbah",
        "state": "NSW",
        "area": "tweed-valley",
        "type": "major_town",
        "intro": "Murwillumbah is the commercial heart of the Tweed Valley, with government services, retail, and creative studios lining the banks of the Tweed River. Heritage buildings sit beside modern industrial estates, creating diverse technology needs for local teams.",
    },
    {
        "name": "South Murwillumbah",
        "state": "NSW",
        "area": "tweed-valley",
        "type": "industrial",
        "intro": "South Murwillumbah houses bustling industrial estates, food manufacturers, and logistics hubs supporting the wider Tweed. Businesses balance floodplain considerations with the need for streamlined operations and dependable data systems.",
    },
    {
        "name": "Bray Park",
        "state": "NSW",
        "area": "tweed-valley",
        "type": "suburban",
        "intro": "Bray Park is a residential and light industrial pocket on the edge of Murwillumbah, home to trades, service businesses, and community organisations. Reliable networks keep teams connected between home offices and nearby worksites.",
    },
    {
        "name": "Byangum",
        "state": "NSW",
        "area": "tweed-valley",
        "type": "rural_locality",
        "intro": "Byangum is a quiet riverside village west of Murwillumbah, surrounded by sugarcane farms and lifestyle properties. Home-based businesses and growers require robust technology despite limited local infrastructure.",
    },
    {
        "name": "Fernvale",
        "state": "NSW",
        "area": "tweed-valley",
        "type": "rural_locality",
        "intro": "Fernvale sits amid fertile farmland south of Murwillumbah, where producers and contractors manage operations across sheds, packing rooms, and remote paddocks. Dependable connectivity supports everything from irrigation controls to finance platforms.",
    },
    {
        "name": "Condong",
        "state": "NSW",
        "area": "tweed-river",
        "type": "industrial",
        "intro": "Condong is known for its sugar mill and supporting agribusinesses clustered along the Tweed River. Teams juggle heavy industry requirements with modern reporting and compliance expectations.",
    },
    {
        "name": "Tygalgah",
        "state": "NSW",
        "area": "tweed-valley",
        "type": "rural_locality",
        "intro": "Tygalgah is a small rural locality near Murwillumbah where cane farms and rural enterprises stretch across the floodplain. Technology must withstand seasonal weather while keeping data secure.",
    },
    {
        "name": "North Arm",
        "state": "NSW",
        "area": "tweed-valley",
        "type": "rural_locality",
        "intro": "North Arm encompasses rolling farmland and acreage properties north of Murwillumbah. Landholders and consultants rely on cloud tools to coordinate suppliers, finance, and environmental reporting.",
    },
    {
        "name": "Kynnumboon",
        "state": "NSW",
        "area": "tweed-valley",
        "type": "rural_locality",
        "intro": "Kynnumboon is a scenic pocket along the Tweed River featuring cane fields, grazing land, and rural homesteads. Keeping business records and monitoring equipment online is critical for seasonal planning.",
    },
    {
        "name": "Dunbible",
        "state": "NSW",
        "area": "tweed-valley",
        "type": "rural_locality",
        "intro": "Dunbible sits just south of Murwillumbah, blending small farms with rural residential enclaves. Local trades and producers depend on reliable devices and data sharing to coordinate projects.",
    },
    {
        "name": "Dungay",
        "state": "NSW",
        "area": "tweed-valley",
        "type": "rural_locality",
        "intro": "Dungay spans fertile valley land dotted with horticulture and dairy operations. Seasonal workers and family businesses need secure access to cloud records and communications tools.",
    },
    {
        "name": "Eungella",
        "state": "NSW",
        "area": "tweed-hinterland",
        "type": "hinterland_village",
        "intro": "Eungella sits in the foothills above Murwillumbah, combining rainforest retreats with hobby farms and creative studios. Patchy connectivity makes resilient technology essential for customer service.",
    },
    {
        "name": "Nobbys Creek",
        "state": "NSW",
        "area": "tweed-hinterland",
        "type": "rural_locality",
        "intro": "Nobbys Creek is a lush hinterland locality west of Murwillumbah with acreage homes, growers, and retreat operators. Residents depend on hybrid connectivity solutions to keep business platforms available.",
    },
    {
        "name": "Smiths Creek",
        "state": "NSW",
        "area": "tweed-hinterland",
        "type": "rural_locality",
        "intro": "Smiths Creek winds through forested gullies and farmland between Uki and Stokers Siding. Operators juggle creative enterprises and primary production, requiring flexible, secure technology.",
    },
    {
        "name": "Crystal Creek",
        "state": "NSW",
        "area": "tweed-forests",
        "type": "hinterland_village",
        "intro": "Crystal Creek is renowned for its rainforest retreats and boutique accommodation tucked beneath Wollumbin. Visitors expect premium experiences backed by reliable digital services.",
    },
    {
        "name": "Upper Crystal Creek",
        "state": "NSW",
        "area": "tweed-forests",
        "type": "hinterland_village",
        "intro": "Upper Crystal Creek offers secluded lodges and wellness escapes amid ancient rainforest. Luxury operators rely on strong connectivity and privacy-focused systems to delight guests.",
    },
    {
        "name": "Chillingham",
        "state": "NSW",
        "area": "tweed-hinterland",
        "type": "hinterland_village",
        "intro": "Chillingham is a gateway village between the Tweed and the Scenic Rim, supporting growers, artisans, and eco-tourism ventures. Businesses blend roadside trading with online marketing and bookings.",
    },
    {
        "name": "Limpinwood",
        "state": "NSW",
        "area": "tweed-hinterland",
        "type": "rural_locality",
        "intro": "Limpinwood features rainforest properties, macadamia farms, and nature retreats along the Tweed Range. Operators need dependable systems that can run across dispersed buildings.",
    },
    {
        "name": "Tyalgum",
        "state": "NSW",
        "area": "tweed-hinterland",
        "type": "hinterland_village",
        "intro": "Tyalgum is a vibrant hinterland village known for its creative scene, boutique shops, and destination weddings. Reliable connectivity keeps events, accommodation, and retail experiences humming.",
    },
    {
        "name": "Tyalgum Creek",
        "state": "NSW",
        "area": "tweed-hinterland",
        "type": "rural_locality",
        "intro": "Tyalgum Creek stretches across rural properties and forested valleys beside the Oxley River. Landholders and retreats require cloud systems that cope with variable power and connectivity.",
    },
    {
        "name": "Zara",
        "state": "NSW",
        "area": "tweed-hinterland",
        "type": "rural_locality",
        "intro": "Zara is a secluded locality near Wollumbin National Park where lifestyle acreage meets productive farmland. Operators juggle tourism bookings with on-property management.",
    },
    {
        "name": "Pumpenbil",
        "state": "NSW",
        "area": "tweed-hinterland",
        "type": "rural_locality",
        "intro": "Pumpenbil consists of rolling farmland and forest gullies west of Tyalgum. Primary producers and contractors coordinate crews across challenging terrain.",
    },
    {
        "name": "Brays Creek",
        "state": "NSW",
        "area": "tweed-hinterland",
        "type": "rural_locality",
        "intro": "Brays Creek lies along the Tweed Range Road with dairy farms, produce stalls, and rural cottages. Cloud-based tools help residents manage orders and compliance reporting.",
    },
    {
        "name": "Kunghur",
        "state": "NSW",
        "area": "tweed-hinterland",
        "type": "hinterland_village",
        "intro": "Kunghur overlooks Clarrie Hall Dam and supports a tight-knit community of farmers, creatives, and outdoor operators. Connectivity and data security underpin bookings and remote management.",
    },
    {
        "name": "Kunghur Creek",
        "state": "NSW",
        "area": "tweed-hinterland",
        "type": "rural_locality",
        "intro": "Kunghur Creek spans dense forest and farmland south of Clarrie Hall Dam. Enterprises depend on reliable backups and communications that reach field teams.",
    },
    {
        "name": "Mount Warning (Wollumbin)",
        "state": "NSW",
        "area": "tweed-forests",
        "type": "hinterland_village",
        "intro": "Mount Warning, known as Wollumbin, anchors the Tweed caldera and draws thousands of visitors each year. Local guides, accommodation providers, and cultural enterprises need secure, high-availability systems.",
    },
    {
        "name": "Mount Burrell",
        "state": "NSW",
        "area": "tweed-hinterland",
        "type": "rural_locality",
        "intro": "Mount Burrell covers rugged hinterland west of Uki with farms, eco-villages, and small retailers. Operators balance off-grid living with the need for dependable communications.",
    },
    {
        "name": "Doon Doon",
        "state": "NSW",
        "area": "tweed-hinterland",
        "type": "rural_locality",
        "intro": "Doon Doon looks over Clarrie Hall Dam and the Tweed Valley, with residents managing farms, retreats, and creative workshops. Technology must cope with remote settings and seasonal tourism.",
    },
    {
        "name": "Commissioners Creek",
        "state": "NSW",
        "area": "tweed-hinterland",
        "type": "rural_locality",
        "intro": "Commissioners Creek features densely forested ridges and rural holdings south of Tyalgum. Businesses rely on flexible IT solutions that can run from homesteads and sheds alike.",
    },
    {
        "name": "Midginbil",
        "state": "NSW",
        "area": "tweed-hinterland",
        "type": "hinterland_village",
        "intro": "Midginbil is home to adventure resorts and rural retreats near the Nightcap Range. Operators juggle large groups, corporate events, and seasonal staff who need secure digital systems.",
    },
    {
        "name": "Terragon",
        "state": "NSW",
        "area": "tweed-hinterland",
        "type": "rural_locality",
        "intro": "Terragon combines rolling farmland with forested escarpments outside Uki. Landholders, artists, and contractors need communications that reach remote studios and worksites.",
    },
    {
        "name": "Uki",
        "state": "NSW",
        "area": "tweed-hinterland",
        "type": "hinterland_village",
        "intro": "Uki is a thriving hinterland village with cafes, markets, and tourism ventures that serve visitors heading to Wollumbin National Park. Technology powers everything from retail transactions to retreat bookings.",
    },
    {
        "name": "Stokers Siding",
        "state": "NSW",
        "area": "tweed-valley",
        "type": "hinterland_village",
        "intro": "Stokers Siding is known for its arts community, gallery spaces, and rural living on the old railway line south of Murwillumbah. Creative businesses require secure digital tools to showcase their work worldwide.",
    },
    {
        "name": "Burringbar",
        "state": "NSW",
        "area": "tweed-valley",
        "type": "hinterland_village",
        "intro": "Burringbar is a village on the Tweed Valley Way with cafes, vintage retailers, and surrounding farms. Local enterprises blend main-street hospitality with online sales and bookings.",
    },
    {
        "name": "Mooball",
        "state": "NSW",
        "area": "tweed-valley",
        "type": "hinterland_village",
        "intro": "Mooball offers a mix of roadside diners, farming properties, and lifestyle acreage south of Burringbar. Businesses count on technology to manage logistics and traveller expectations.",
    },
    {
        "name": "Crabbes Creek",
        "state": "NSW",
        "area": "tweed-valley",
        "type": "rural_locality",
        "intro": "Crabbes Creek spans farmland and coastal foothills between Burringbar and the Tweed Coast. Producers and home-based entrepreneurs need resilient systems to stay connected.",
    },
    {
        "name": "Sleepy Hollow",
        "state": "NSW",
        "area": "tweed-valley",
        "type": "rural_locality",
        "intro": "Sleepy Hollow is a peaceful locality tucked between cane fields and forest near the Tweed Coast. Residents juggle rural living with digital business operations.",
    },
    {
        "name": "Reserve Creek",
        "state": "NSW",
        "area": "tweed-valley",
        "type": "rural_locality",
        "intro": "Reserve Creek lies between Murwillumbah and the coastal villages, with tropical fruit farms and nurseries lining the valley. Growers and distributors depend on cloud platforms for sales and logistics.",
    },
    {
        "name": "Kielvale",
        "state": "NSW",
        "area": "tweed-valley",
        "type": "rural_locality",
        "intro": "Kielvale neighbours Murwillumbah with a blend of rural residential lots and small-scale agriculture. Local contractors and service businesses rely on streamlined communications and data security.",
    },
    {
        "name": "Nunderi",
        "state": "NSW",
        "area": "tweed-valley",
        "type": "rural_locality",
        "intro": "Nunderi sits on the ridge between the Tweed Coast and Murwillumbah, offering sweeping views and acreage properties. Residents split time between home offices, workshops, and coastal job sites.",
    },
    {
        "name": "Wardrop Valley",
        "state": "NSW",
        "area": "tweed-valley",
        "type": "rural_locality",
        "intro": "Wardrop Valley combines light industry with farmland south of Murwillumbah. Manufacturers and trades require robust connectivity to coordinate deliveries and compliance.",
    },
    {
        "name": "Eviron",
        "state": "NSW",
        "area": "tweed-coast",
        "type": "rural_locality",
        "intro": "Eviron overlooks the Tweed Coast and hosts turf farms, nurseries, and rural acreage homes. Operators balance field work with cloud-based scheduling and logistics.",
    },
    {
        "name": "Clothiers Creek",
        "state": "NSW",
        "area": "tweed-coast",
        "type": "rural_locality",
        "intro": "Clothiers Creek is set in the coastal hinterland with macadamia farms, nurseries, and boutique accommodation. Teams depend on fast, secure access to cloud systems from ridge-top properties.",
    },
    {
        "name": "Farrants Hill",
        "state": "NSW",
        "area": "tweed-coast",
        "type": "rural_locality",
        "intro": "Farrants Hill is a picturesque ridge between the Tweed Coast and the valley, dotted with acreage homes and small-scale agribusiness. Residents require reliable connectivity for remote work and property management.",
    },
    {
        "name": "Glengarrie",
        "state": "NSW",
        "area": "tweed-coast",
        "type": "rural_locality",
        "intro": "Glengarrie sits just inland from the Tweed Coast Highway with a mix of farms, warehouses, and lifestyle properties. Businesses interface with both coastal and valley supply chains.",
    },
    {
        "name": "Urliup",
        "state": "NSW",
        "area": "tweed-rural",
        "type": "rural_locality",
        "intro": "Urliup is a secluded valley south of the Tweed River featuring rainforest conservation areas and eco-retreats. Operators coordinate teams across multiple buildings and remote monitoring sites.",
    },
    {
        "name": "Duroby",
        "state": "NSW",
        "area": "tweed-rural",
        "type": "rural_locality",
        "intro": "Duroby is a rural enclave between Bilambil and Terranora with small farms and acreage homes. Residents combine home offices with contracting work along the coast.",
    },
    {
        "name": "Upper Duroby",
        "state": "NSW",
        "area": "tweed-rural",
        "type": "rural_locality",
        "intro": "Upper Duroby stretches across rolling hills overlooking the Tweed River. Landholders require resilient networks to manage irrigation, finance, and compliance from remote locations.",
    },
    {
        "name": "Carool",
        "state": "NSW",
        "area": "tweed-rural",
        "type": "hinterland_village",
        "intro": "Carool is perched high above the Tweed Valley with vineyards, orchards, and panoramic accommodation. Tourism operators and growers depend on cloud systems that handle bookings and export logistics.",
    },
    {
        "name": "Tomewin",
        "state": "NSW",
        "area": "tweed-rural",
        "type": "rural_locality",
        "intro": "Tomewin straddles the NSW–QLD border with rainforest reserves, avocado farms, and scenic lookouts. Businesses require hybrid connectivity solutions and secure cross-border collaboration.",
    },
    {
        "name": "Tumbulgum",
        "state": "NSW",
        "area": "tweed-river",
        "type": "river_village",
        "intro": "Tumbulgum is a heritage river village where cafes, pubs, and tourism operators overlook the Tweed and Rous Rivers. Visitors expect reliable digital experiences alongside waterfront charm.",
    },
    {
        "name": "Dulguigan",
        "state": "NSW",
        "area": "tweed-river",
        "type": "rural_locality",
        "intro": "Dulguigan lies on the Tweed River floodplain north of Murwillumbah with cane farms and rural residences. Operators need dependable systems that protect data through seasonal weather.",
    },
    {
        "name": "Kings Forest",
        "state": "NSW",
        "area": "tweed-coast",
        "type": "growth_area",
        "intro": "Kings Forest is an emerging master-planned community on the Tweed Coast, bringing together residential development, retail, and environmental conservation. New projects demand scalable technology from the ground up.",
    },
    {
        "name": "Cudgen",
        "state": "NSW",
        "area": "tweed-coast",
        "type": "rural_locality",
        "intro": "Cudgen is home to rich red-soil farms and the Tweed Hospital precinct overlooking Kingscliff. Growers, healthcare teams, and service businesses rely on seamless digital workflows.",
    },
    {
        "name": "Chinderah",
        "state": "NSW",
        "area": "tweed-river",
        "type": "river_village",
        "intro": "Chinderah sits on the banks of the Tweed River with holiday parks, marine businesses, and highway service centres. Operators juggle drive-by customers and long-stay guests who expect reliable connectivity.",
    },
    {
        "name": "Chinderah Bay",
        "state": "NSW",
        "area": "tweed-river",
        "type": "river_village",
        "intro": "Chinderah Bay is a quiet waterfront enclave beside Chinderah that attracts anglers, grey nomads, and boutique accommodation. Maintaining guest services depends on dependable digital platforms.",
    },
    {
        "name": "Cudgera Creek",
        "state": "NSW",
        "area": "tweed-coast",
        "type": "rural_locality",
        "intro": "Cudgera Creek winds from the hinterland to the coast near Pottsville, with farms, eco-stays, and residential estates along the way. Connectivity and data security keep bookings and logistics in sync.",
    },
    {
        "name": "Duranbah",
        "state": "NSW",
        "area": "tweed-coast",
        "type": "rural_locality",
        "intro": "Duranbah covers both a rural locality and a famed surf break on the Tweed Coast. Agricultural enterprises and tourism operators alike need consistent technology to manage operations.",
    },
    {
        "name": "Tanglewood",
        "state": "NSW",
        "area": "tweed-coast",
        "type": "rural_locality",
        "intro": "Tanglewood offers acreage living and eco-retreats tucked behind the coastal dunes near Pottsville. Residents and operators require networks that can stretch across large properties.",
    },
    {
        "name": "Round Mountain",
        "state": "NSW",
        "area": "tweed-coast",
        "type": "rural_locality",
        "intro": "Round Mountain sits between Cabarita Beach and the hinterland, home to macadamia farms, equine facilities, and new residential estates. Reliable connectivity keeps projects and bookings aligned.",
    },
    {
        "name": "Casuarina",
        "state": "NSW",
        "area": "tweed-coast",
        "type": "coastal_suburb",
        "intro": "Casuarina is a fast-growing coastal suburb with beach resorts, dining precincts, and premium housing. Businesses cater to visitors and residents who expect seamless digital experiences.",
    },
    {
        "name": "Bogangar (Cabarita Beach)",
        "state": "NSW",
        "area": "tweed-coast",
        "type": "coastal_village",
        "intro": "Bogangar, known as Cabarita Beach, blends surf culture with boutique accommodation and dining. Operators rely on modern technology to manage bookings and guest services year-round.",
    },
    {
        "name": "Hastings Point",
        "state": "NSW",
        "area": "tweed-coast",
        "type": "coastal_village",
        "intro": "Hastings Point is a tranquil seaside hamlet with holiday parks, eco-resorts, and marine tours. Businesses balance seasonal demand with the need for always-on connectivity.",
    },
    {
        "name": "Pottsville",
        "state": "NSW",
        "area": "tweed-coast",
        "type": "coastal_suburb",
        "intro": "Pottsville combines family-friendly beaches with a thriving main street of cafes, health services, and retail. Growing neighbourhoods require scalable technology support.",
    },
    {
        "name": "Wooyung",
        "state": "NSW",
        "area": "tweed-coast",
        "type": "coastal_village",
        "intro": "Wooyung offers unspoilt beaches, campgrounds, and eco-retreats at the southern edge of the Tweed Coast. Guests expect reliable online booking and smooth on-site connectivity.",
    },
    {
        "name": "Kingscliff",
        "state": "NSW",
        "area": "tweed-coast",
        "type": "coastal_suburb",
        "intro": "Kingscliff is a bustling coastal centre with resorts, specialty retail, and the Tweed Valley Hospital precinct. Businesses serve locals and visitors who expect enterprise-grade connectivity.",
    },
    {
        "name": "Fingal Head",
        "state": "NSW",
        "area": "tweed-coast",
        "type": "coastal_village",
        "intro": "Fingal Head is a picturesque village at the Tweed River entrance, popular with surfers, holidaymakers, and cultural tours. Operators need secure systems to manage bookings and visitor services.",
    },
    {
        "name": "Terranora",
        "state": "NSW",
        "area": "tweed-heads",
        "type": "suburban",
        "intro": "Terranora is a ridge-top community overlooking the Tweed River, blending schools, sporting clubs, and home-based businesses. Connectivity links households with the Tweed Heads commercial centres.",
    },
    {
        "name": "Banora Point",
        "state": "NSW",
        "area": "tweed-heads",
        "type": "suburban",
        "intro": "Banora Point is a major residential and commercial hub just south of the Queensland border. Healthcare providers, professional services, and clubs depend on responsive local IT expertise.",
    },
    {
        "name": "Bilambil",
        "state": "NSW",
        "area": "tweed-rural",
        "type": "rural_locality",
        "intro": "Bilambil stretches from the Terranora Broadwater to rolling hinterland hills, with farms, schools, and creative enterprises spread throughout. Technology connects classrooms, studios, and paddocks.",
    },
    {
        "name": "Bilambil Heights",
        "state": "NSW",
        "area": "tweed-heads",
        "type": "suburban",
        "intro": "Bilambil Heights overlooks the Tweed River and Gold Coast skyline, home to growing residential estates and home-based professionals. Reliable digital tools support remote work and cross-border clients.",
    },
    {
        "name": "Cobaki",
        "state": "NSW",
        "area": "tweed-heads",
        "type": "rural_locality",
        "intro": "Cobaki features wetlands, acreage homes, and emerging developments minutes from the Gold Coast Airport. Businesses balance environmental considerations with fast-paced project timelines.",
    },
    {
        "name": "Cobaki Lakes",
        "state": "NSW",
        "area": "tweed-heads",
        "type": "growth_area",
        "intro": "Cobaki Lakes is a planned community on the Tweed-Queensland border, set to include residential neighbourhoods, schools, and commercial precincts. Digital infrastructure is vital from the earliest construction stages.",
    },
    {
        "name": "Tweed Heads",
        "state": "NSW",
        "area": "tweed-heads",
        "type": "major_town",
        "intro": "Tweed Heads is the gateway city of the NSW North Coast, encompassing major retail centres, healthcare campuses, and government services. Businesses operate across both sides of the state border each day.",
    },
    {
        "name": "Tweed Heads South",
        "state": "NSW",
        "area": "tweed-heads",
        "type": "suburban",
        "intro": "Tweed Heads South hosts bulky goods retail, medical specialists, and light industrial estates serving the wider border region. Teams need integrated systems that connect storefronts, warehouses, and mobile staff.",
    },
    {
        "name": "Tweed Heads West",
        "state": "NSW",
        "area": "tweed-heads",
        "type": "suburban",
        "intro": "Tweed Heads West borders the Terranora Broadwater and the Gold Coast Airport precinct. Aviation suppliers, marine services, and residential communities rely on rapid-response IT support.",
    },
    {
        "name": "Coolangatta",
        "state": "QLD",
        "area": "gold-coast-coastal",
        "type": "gold_coast_coastal",
        "intro": "Coolangatta anchors the southern Gold Coast with iconic beaches, international tourism, and a vibrant dining precinct. Cross-border operators require technology that performs during peak visitor seasons.",
    },
    {
        "name": "Bilinga",
        "state": "QLD",
        "area": "gold-coast-coastal",
        "type": "gold_coast_coastal",
        "intro": "Bilinga surrounds the Gold Coast Airport and beachfront accommodations, blending aviation services with holiday rentals. Operators manage complex logistics and guest expectations simultaneously.",
    },
    {
        "name": "Tugun",
        "state": "QLD",
        "area": "gold-coast-coastal",
        "type": "gold_coast_coastal",
        "intro": "Tugun is a laid-back coastal suburb with cafes, health clinics, and beachfront accommodation. Reliable digital systems support businesses catering to both locals and travellers.",
    },
    {
        "name": "Currumbin",
        "state": "QLD",
        "area": "gold-coast-coastal",
        "type": "gold_coast_coastal",
        "intro": "Currumbin is famous for its wildlife sanctuary, surf clubs, and creekside dining. Local enterprises juggle tourism, retail, and professional services with high expectations for uptime.",
    },
    {
        "name": "Currumbin Waters",
        "state": "QLD",
        "area": "gold-coast-suburb",
        "type": "gold_coast_suburb",
        "intro": "Currumbin Waters spans residential canals, light industrial estates, and service businesses behind the coastline. Teams collaborate across warehouses, home offices, and customer sites.",
    },
    {
        "name": "Currumbin Valley",
        "state": "QLD",
        "area": "gold-coast-hinterland",
        "type": "gold_coast_hinterland",
        "intro": "Currumbin Valley is a lush hinterland escape with wellness retreats, organic farms, and eco-accommodation. Operators rely on digital bookings and cloud collaboration despite limited infrastructure.",
    },
    {
        "name": "Elanora",
        "state": "QLD",
        "area": "gold-coast-suburb",
        "type": "gold_coast_suburb",
        "intro": "Elanora is a family-friendly suburb with schools, shopping centres, and professional services supporting the southern Gold Coast. Businesses need reliable systems to serve commuters and remote workers alike.",
    },
    {
        "name": "Tallebudgera",
        "state": "QLD",
        "area": "gold-coast-suburb",
        "type": "gold_coast_suburb",
        "intro": "Tallebudgera covers both creekside suburbs and acreage living close to Burleigh Heads. Education providers, trades, and lifestyle brands require secure technology for hybrid teams.",
    },
    {
        "name": "Tallebudgera Valley",
        "state": "QLD",
        "area": "gold-coast-hinterland",
        "type": "gold_coast_hinterland",
        "intro": "Tallebudgera Valley is dotted with equestrian centres, retreats, and holiday homes tucked into the hinterland. Connectivity solutions must bridge large properties and seasonal staff turnover.",
    },
    {
        "name": "Palm Beach",
        "state": "QLD",
        "area": "gold-coast-coastal",
        "type": "gold_coast_coastal",
        "intro": "Palm Beach combines a thriving dining scene with beachfront apartments and professional services. Businesses rely on high-speed networks to support residents and visitors.",
    },
    {
        "name": "Piggabeen",
        "state": "QLD",
        "area": "gold-coast-hinterland",
        "type": "gold_coast_hinterland",
        "intro": "Piggabeen is a rural pocket straddling the NSW border with farms, acreages, and lifestyle retreats. Operators balance peaceful surroundings with the need for dependable digital tools.",
    },
]


def build_description(name: str, area: str) -> str:
    if name == "Tweed Shire":
        return "Comprehensive managed IT, cloud, and cyber security services for organisations across the Tweed Shire."
    region_text = region_descriptions.get(area, "across the region")
    return f"Managed IT, cloud, and cyber security support for {name} businesses {region_text}."


def write_index():
    lines = [
        "---",
        'title: "Locations | Tweed Cloud"',
        'description: "Discover the Tweed Cloud service areas across the Tweed Shire and southern Gold Coast."',
        f'image: "{IMAGE_PATH}"',
        "---",
        "",
        "## Local IT support across the Tweed and southern Gold Coast",
        "",
        "Tweed Cloud partners with businesses throughout the Tweed Shire in New South Wales and the neighbouring suburbs of the southern Gold Coast. Explore the dedicated service pages below to learn how we tailor managed IT, cloud, and cyber security solutions for your community.",
        "",
    ]
    content = "\n".join(lines)
    (CONTENT_DIR / "_index.md").write_text(content, encoding="utf-8")


def render_page(location: dict) -> str:
    name = location["name"]
    area = location["area"]
    loc_type = location["type"]
    description = build_description(name, area)
    intro = location["intro"]
    services = type_service_paragraphs[loc_type].format(name=name)
    bullets = "\n".join(f"- {item}" for item in type_bullets[loc_type])
    closing = area_closing[area]
    region_text = region_descriptions.get(area, "across the region")

    lines = [
        "---",
        f'title: "IT Support in {name} | Tweed Cloud"',
        f'description: "{description}"',
        f'image: "{IMAGE_PATH}"',
        "---",
        "",
        f"## Working with businesses in {name}",
        intro,
        "",
        f"## How we help {name} organisations grow",
        services,
        "",
        f"### Popular solutions for {name}",
    ]
    lines.extend(f"- {item}" for item in type_bullets[loc_type])
    lines.extend(
        [
            "",
            f"## Connected support {region_text}",
            f"{closing} Ready to modernise your technology in {name}? [Book a consultation](/consultation/) with our Tweed-based specialists.",
            "",
        ]
    )
    return "\n".join(lines)


def main():
    write_index()
    for location in locations:
        slug = location.get("slug") or slugify(location["name"])
        path = CONTENT_DIR / f"{slug}.md"
        path.write_text(render_page(location), encoding="utf-8")


if __name__ == "__main__":
    main()
