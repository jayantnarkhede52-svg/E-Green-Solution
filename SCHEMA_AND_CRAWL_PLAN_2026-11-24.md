# E Green Solution: schema and crawl architecture plan

Date: 24 November 2026. Scope: the 45 canonical URLs in the local sitemap, plus the unpublished Journey page. This is a plan, not a claim that the proposed markup has been deployed or validated by Google. The existing schema column is a local JSON-LD inventory; syntactically valid JSON alone does not establish correctness or eligibility.

## Principles

- Use one consistent business entity, name, confirmed Pune address, telephone and stable `@id`; do not describe the same office as a separate location in each service area. The user confirmed the website's address and published project and warranty details. Confirm business hours and social profile URLs before adding them.
- Six locality pages currently contain `SolarEnergyContractor`, which returned 404 from schema.org on 24 November. Replace that type with an appropriate recognized `HomeAndConstructionBusiness` or `LocalBusiness` entity, and have each page's `Service` reference the shared business. Review their varying business names and review counts rather than treating them as separate branches.
- LocalBusiness review snippets for a business reviewing itself are not eligible for Google's local-business review feature. Remove or correct site-owned `aggregateRating` markup unless independently supported and appropriate; do not fabricate ratings. See https://developers.google.com/search/docs/appearance/structured-data/local-business
- `Service`, `WebPage`, `CollectionPage` and `ItemList` may describe content but do not guarantee a Google rich result. Keep only useful and accurate entities, grounded in visible page content. Breadcrumb structured data must match a real visible breadcrumb and canonical URL.
- FAQ content can be useful to visitors, but Google no longer shows FAQ rich results. Existing `FAQPage` markup is optional and should only remain if its answers match the visible page; do not add it for a promised Google enhancement. https://developers.google.com/search/updates
- `Article` / `BlogPosting`: use real headline, accessible representative image, author, publisher and accurate publication and substantive modification dates. Project pages qualify as articles only when their visible content actually functions as an editorial case study. Do not infer commissioning dates.
- `VideoObject`: consider only for actual publicly playable videos with a crawlable thumbnail, valid name, description and genuine upload date. Add `contentUrl` or `embedUrl` when appropriate. If dates are unknown, defer it. https://developers.google.com/search/docs/appearance/structured-data/video
- Do not add broad Product or Offer markup for a general service or an unsubstantiated price range; review the current water-heater Product and AggregateOffer against visible, specific offers. No schema guarantees rankings, indexing or rich results.

## Page-by-page schema map

B = BreadcrumbList; S = Service; A = Article or BlogPosting. Existing types are shown as detected; proposals marked optional require evidence and a useful purpose.

| Canonical page | Existing schema | Proposed plan |
| --- | --- | --- |
| `/` | HomeAndConstructionBusiness, Service, Organization, BreadcrumbList, WebPage, FAQPage | Keep the verified business entity and Organization; reconcile their IDs. Review WebPage, Service and FAQ against visible content. |
| `/solar-panel-pune` | LocalBusiness, Service, BreadcrumbList | Keep B + S and link business identity to the verified shared business; reconcile duplicate entity IDs. |
| `/services` | BreadcrumbList, Service | Keep B + S; connect provider to the verified business and match the visible service scope. |
| `/residential-solar` | Service, BreadcrumbList | Keep B + S; connect provider to the verified business and match the visible service scope. |
| `/commercial-solar-pune` | Service, BreadcrumbList, FAQPage | Keep B + S; connect provider to the verified business and match the visible service scope. Review existing FAQPage for accuracy. |
| `/industrial-solar` | Service, BreadcrumbList | Keep B + S; connect provider to the verified business and match the visible service scope. |
| `/solar-water-heater-pune` | Product, Service, BreadcrumbList, FAQPage | Keep B + S; review Product and price offers against an actual visible, specific offer. Review FAQ content. |
| `/calculator` | BreadcrumbList | Keep B; optional WebPage or ContactPage only when it describes the visible page. |
| `/projects` | BreadcrumbList | Keep B; CollectionPage or ItemList is optional if it accurately represents visible case studies. |
| `/projects/eagle-burgmann-200kw-solar-pune` | Article, BreadcrumbList | Keep B + Article if the case study is editorial; verify project facts and dates. |
| `/projects/konark-a-plus-100kw-housing-society-solar-pune` | Article, BreadcrumbList | Keep B + Article if the case study is editorial; verify project facts and dates. Consider VideoObject only after required video facts are confirmed. |
| `/areas` | Service, BreadcrumbList, ItemList | Keep B, S and ItemList if the list matches visible service areas; reference the shared business. |
| `/gallery` | BreadcrumbList | Keep B; add VideoObject only for qualifying videos with confirmed metadata, preferably on dedicated watch pages. |
| `/about` | BreadcrumbList | Keep B; optional WebPage or ContactPage only when it describes the visible page. |
| `/contact` | BreadcrumbList | Keep B; optional WebPage or ContactPage only when it describes the visible page. |
| `/solar-guide` | None | Consider B if a visible breadcrumb is provided; use WebPage only if useful. Do not invent an Article date. |
| `/privacy-policy` | None | No special rich-result markup needed; add B only if a matching visible breadcrumb exists. |
| `/solar-panel-cleaning-pune` | BreadcrumbList, Service, FAQPage | Keep B + S; connect provider to the verified business and match the visible service scope. Review existing FAQPage for accuracy. |
| `/solar-amc-pune` | BreadcrumbList, Service, FAQPage | Keep B + S; connect provider to the verified business and match the visible service scope. Review existing FAQPage for accuracy. |
| `/solar-repair-maintenance-pune` | BreadcrumbList, Service, FAQPage | Keep B + S; connect provider to the verified business and match the visible service scope. Review existing FAQPage for accuracy. |
| `/solar-inverter-repair-pune` | BreadcrumbList, Service, FAQPage | Keep B + S; connect provider to the verified business and match the visible service scope. Review existing FAQPage for accuracy. |
| `/solar-net-meter-msedcl-pune` | BreadcrumbList, Service, FAQPage | Keep B + S; connect provider to the verified business and match the visible service scope. Review existing FAQPage for accuracy. |
| `/solar-plant-revamping-repowering` | BreadcrumbList, Service, FAQPage | Keep B + S; connect provider to the verified business and match the visible service scope. Review existing FAQPage for accuracy. |
| `/solar-panel-chakan` | LocalBusiness, SolarEnergyContractor, Service, BreadcrumbList, FAQPage | Keep B + S; replace invalid SolarEnergyContractor, reference the shared business, and review ratings and business identity. Review FAQ content. |
| `/solar-panel-pimpri-chinchwad` | LocalBusiness, SolarEnergyContractor, Service, BreadcrumbList, FAQPage | Keep B + S; replace invalid SolarEnergyContractor, reference the shared business, and review ratings and business identity. Review FAQ content. |
| `/solar-panel-baner-bavdhan` | LocalBusiness, SolarEnergyContractor, Service, BreadcrumbList, FAQPage | Keep B + S; replace invalid SolarEnergyContractor, reference the shared business, and review ratings and business identity. Review FAQ content. |
| `/solar-panel-bhosari-pcmc` | LocalBusiness, SolarEnergyContractor, Service, BreadcrumbList, FAQPage | Keep B + S; replace invalid SolarEnergyContractor, reference the shared business, and review ratings and business identity. Review FAQ content. |
| `/solar-panel-kiwale` | LocalBusiness, SolarEnergyContractor, Service, BreadcrumbList, FAQPage | Keep B + S; replace invalid SolarEnergyContractor, reference the shared business, and review ratings and business identity. Review FAQ content. |
| `/solar-panel-lonavala` | LocalBusiness, SolarEnergyContractor, Service, BreadcrumbList, FAQPage | Keep B + S; replace invalid SolarEnergyContractor, reference the shared business, and review ratings and business identity. Review FAQ content. |
| `/blog` | BreadcrumbList, CollectionPage | Keep B + CollectionPage; verify its list reflects visible linked articles. |
| `/blog/bifacial-solar-panels-pune` | BreadcrumbList, BlogPosting, FAQPage | Keep B + BlogPosting; verify author, dates, image and visible content. Review existing FAQPage for accuracy; no FAQ rich result. |
| `/blog/mono-perc-vs-topcon-solar-pune` | BreadcrumbList, BlogPosting, FAQPage | Keep B + BlogPosting; verify author, dates, image and visible content. Review existing FAQPage for accuracy; no FAQ rich result. |
| `/blog/dcr-solar-panels-pune` | BreadcrumbList, BlogPosting, FAQPage | Keep B + BlogPosting; verify author, dates, image and visible content. Review existing FAQPage for accuracy; no FAQ rich result. |
| `/blog/hybrid-solar-system-lithium-battery-pune` | BreadcrumbList, BlogPosting, FAQPage | Keep B + BlogPosting; verify author, dates, image and visible content. Review existing FAQPage for accuracy; no FAQ rich result. |
| `/blog/enphase-microinverter-installers-pune` | BreadcrumbList, BlogPosting, FAQPage | Keep B + BlogPosting; verify author, dates, image and visible content. Review existing FAQPage for accuracy; no FAQ rich result. |
| `/blog/on-grid-solar-inverter-dealers-pune` | BreadcrumbList, BlogPosting, FAQPage | Keep B + BlogPosting; verify author, dates, image and visible content. Review existing FAQPage for accuracy; no FAQ rich result. |
| `/blog/elevated-rooftop-solar-structure-pune` | BreadcrumbList, BlogPosting, FAQPage | Keep B + BlogPosting; verify author, dates, image and visible content. Review existing FAQPage for accuracy; no FAQ rich result. |
| `/blog/housing-society-solar-pune-rules-subsidy` | BreadcrumbList, BlogPosting | Keep B + BlogPosting; verify author, dates, image and visible content. |
| `/blog/3kw-vs-5kw-solar-price-pune-subsidy` | BreadcrumbList, BlogPosting, FAQPage | Keep B + BlogPosting; verify author, dates, image and visible content. Review existing FAQPage for accuracy; no FAQ rich result. |
| `/blog/msedcl-solar-net-metering-pune-delays-process` | BreadcrumbList, BlogPosting, FAQPage | Keep B + BlogPosting; verify author, dates, image and visible content. Review existing FAQPage for accuracy; no FAQ rich result. |
| `/blog/solar-generation-dropping-reasons-solutions-pune` | BreadcrumbList, BlogPosting, FAQPage | Keep B + BlogPosting; verify author, dates, image and visible content. Review existing FAQPage for accuracy; no FAQ rich result. |
| `/blog/solar-ready-home-construction-pune` | BreadcrumbList, BlogPosting | Keep B + BlogPosting; verify author, dates, image and visible content. |
| `/blog/msedcl-solar-bill-explained-pune` | BreadcrumbList, BlogPosting | Keep B + BlogPosting; verify author, dates, image and visible content. |
| `/blog/does-solar-work-during-power-cut-pune` | BreadcrumbList, BlogPosting | Keep B + BlogPosting; verify author, dates, image and visible content. |
| `/blog/solar-panel-warranty-india-pune-guide` | BreadcrumbList, BlogPosting | Keep B + BlogPosting; verify author, dates, image and visible content. |

The locally linked `/journey` page is not in the sitemap or deployed. If it becomes a useful indexable page, consider `WebPage` and a matching visible breadcrumb; add `VideoObject` only if its actual video and required facts qualify. The animated canvas alone is not a reason to add video markup.

## Crawlability and URL checks

- All 45 sitemap URLs have a single local self-canonical matching the sitemap. The sitemap paths use hyphens, with no underscores or query parameters. Preserve existing indexed URLs; changing them merely to shorten them can disrupt traffic.
- The local HTML link graph reached all 45 sitemap URLs from the homepage: 29 at depth one and 15 at depth two. All discovered local HTML paths returned a non-error status in this check. This does not prove no unsitemapped or inaccessible orphan exists. `/journey` is linked locally but is not in the sitemap and currently returns 404 in production; ship its file and assets with the local navigation change, then decide whether it should be indexed.
- The live sitemap had 45 successful URL checks and the live homepage had no detected mixed-content subresources in the previous live audit. The local HTML scan found no literal HTTP image, script, stylesheet, video or iframe resources and no images missing an alt attribute. Dynamic resources and CSS need additional production checks. An empty alt can be appropriate for decoration; descriptive alt should explain informative images without keyword stuffing.
- robots.txt advertises the sitemap and blocks `/admin/` and `/solar-hero.html`. A robots block does not itself prevent indexing or protect content, and can hide a noindex directive from Google. Confirm admin authentication and use appropriate crawl/index controls. Static sitemap is sufficient for this small site; Rank Math and WordPress are not required. Submit or inspect it in Search Console after deployment when needed.
- Live apex-to-www redirects currently use 308, a permanent redirect. The old HTTP apex `.html` example took three hops; simplify if hosting configuration supports it without breaking existing URLs. Google may still report previously selected apex canonicals until recrawl.

## Validation and rollout

1. Compare proposed business fields with the confirmed business profile and existing visible pages; verify rating provenance and hours before implementation.
2. Implement one shared identity and page-specific entities in small batches, preserving user content and avoiding duplicate/conflicting nodes.
3. Parse all JSON-LD; check required fields and visible-content consistency; run Schema Markup Validator and Google's Rich Results Test for supported types. Passing a syntax check is not rich-result eligibility.
4. Deploy the verified files, including Journey and new image assets, then recheck production URLs, redirects, canonical tags, robots, sitemap, media and a representative set of rendered pages. Inspect priority pages in Search Console and request indexing only after the live version is ready.
5. Measure field LCP, INP and CLS at the 75th percentile when enough real-user data is available. Local unthrottled timing and Lighthouse lab results do not prove field thresholds. Review mobile navigation and forms on real devices.

## Keyword and content notes

The separate keyword map records an assigned primary phrase, title/description lengths and an approximate exact-phrase share for each sitemap page plus the local Journey page. Density depends on how text and variants are counted and is an editorial diagnostic, not a Google ranking threshold. Google explicitly says it has no optimal keyword density and warns against unnatural repetition: https://developers.google.com/search/help/office-hours/2023/january and https://developers.google.com/search/docs/essentials/spam-policies. The current map does not claim a strict 1.5–2% result for every page.
