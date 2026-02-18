import { createRouter, createWebHistory } from "vue-router";
import PresentationView from "../views/Presentation/PresentationView.vue";
import AboutView from "../views/LandingPages/AboutUs/AboutView.vue";
import ContactView from "../views/LandingPages/ContactUs/ContactView.vue";
import AuthorView from "../views/LandingPages/Author/AuthorView.vue";
import SignInBasicView from "../views/LandingPages/SignIn/BasicView.vue";
import SignUpBasicView from "../views/LandingPages/Signup/BasicView.vue";
import PageHeaders from "../layouts/sections/page-sections/page-headers/HeadersView.vue";
import PageFeatures from "../layouts/sections/page-sections/features/FeaturesView.vue";
import NavigationNavbars from "../layouts/sections/navigation/navbars/NavbarsView.vue";
import NavigationNavTabs from "../layouts/sections/navigation/nav-tabs/NavTabsView.vue";
import NavigationPagination from "../layouts/sections/navigation/pagination/PaginationView.vue";
import InputAreasInputs from "../layouts/sections/input-areas/inputs/InputsView.vue";
import InputAreasForms from "../layouts/sections/input-areas/forms/FormsView.vue";
import ACAlerts from "../layouts/sections/attention-catchers/alerts/AlertsView.vue";
import ACModals from "../layouts/sections/attention-catchers/modals/ModalsView.vue";
import ACTooltipsPopovers from "../layouts/sections/attention-catchers/tooltips-popovers/TooltipsPopoversView.vue";
import ElAvatars from "../layouts/sections/elements/avatars/AvatarsView.vue";
import ElBadges from "../layouts/sections/elements/badges/BadgesView.vue";
import ElBreadcrumbs from "../layouts/sections/elements/breadcrumbs/BreadcrumbsView.vue";
import ElButtons from "../layouts/sections/elements/buttons/ButtonsView.vue";
import ElButtonGroups from "../layouts/sections/elements/button-groups/ButtonGroupsView.vue";
import ElDropdowns from "../layouts/sections/elements/dropdowns/DropdownsView.vue";
import ElProgressBars from "../layouts/sections/elements/progress-bars/ProgressBarsView.vue";
import ElToggles from "../layouts/sections/elements/toggles/TogglesView.vue";
import ElTypography from "../layouts/sections/elements/typography/TypographyView.vue";

// App endpoints
import ManageUsersView from "../views/RentaHouse/Administrator/ManageUsersView.vue";
import ManagePropertiesView from "../views/RentaHouse/Administrator/ManagePropertiesView.vue";
import ExportDatasetView from "../views/RentaHouse/Administrator/ExportDatasetView.vue";
import UserView from "../views/RentaHouse/Profile/UserView.vue";
import RenterManageProperties from "../views/RentaHouse/Renter/RenterManageProperties.vue";
import RenterRecommendedProperties from "../views/RentaHouse/Renter/RenterRecommendedProperties.vue";
import HostManageProperties from "../views/RentaHouse/Host/HostManageProperties.vue";
import Search from "../views/RentaHouse/Guest/Search.vue";
import HostAddProperty from "../views/RentaHouse/Host/HostAddProperty.vue";
import HostPropertyBookings from "../views/RentaHouse/Host/HostPropertyBookings.vue";
import UserInbox from "../views/RentaHouse/Profile/UserInbox.vue";
import UserOutbox from "../views/RentaHouse/Profile/UserOutbox.vue";
import UserCompose from "../views/RentaHouse/Profile/UserCompose.vue";
import HostEditProperty from "../views/RentaHouse/Host/HostEditProperty.vue";
import HostPropertyPage from "../views/RentaHouse/Host/HostPropertyPage.vue";
import RenterEditBooking from "../views/RentaHouse/Renter/RenterEditBooking.vue";
import UserReadMessage from "../views/RentaHouse/Profile/UserReadMessage.vue";
import HostBookingDetails from "../views/RentaHouse/Host/HostBookingDetails.vue";
import UserMyProfile from "../views/RentaHouse/Profile/UserMyProfile.vue";
import UserEditProfile from "../views/RentaHouse/Profile/UserEditProfile.vue";
import ManageUserProfile from "../views/RentaHouse/Administrator/ManageUserProfile.vue";
import RenterBookingDetails from "../views/RentaHouse/Renter/RenterBookingDetails.vue";
import RenterBookingConfirmed from "../views/RentaHouse/Renter/RenterBookingConfirmed.vue";
import RenterCreateBooking from "../views/RentaHouse/Renter/RenterCreateBooking.vue";

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    //
    // Routes for account and session
    //
    {
      path: "/pages/landing-pages/basic",
      name: "signin-basic",
      component: SignInBasicView,
    },

    {
      path: "/pages/landing-pages/basic/signup",
      name: "signup-basic",
      component: SignUpBasicView,
    },

    //
    // Routes for the application
    //
    {
      path: "/administrator/users",
      name: "manage-users",
      component: ManageUsersView,
    },
    {
      path: "/administrator/properties",
      name: "manage-properties",
      component: ManagePropertiesView,
    },
    {
      path: "/administrator/export",
      name: "manage-export",
      component: ExportDatasetView,
    },

    {
      path: "/administrator/user/:id",
      name: "manage-userprofile",
      component: ManageUserProfile,
    },
    // Routes for user
    {
      path: "/user/:id",
      name: "user-profile",
      component: UserView,
    },

    {
      path: "/user/inbox",
      name: "user-inbox",
      component: UserInbox,
    },

    {
      path: "/user/outbox",
      name: "user-outbox",
      component: UserOutbox,
    },

    {
      path: "/user/compose",
      name: "user-compose",
      component: UserCompose,
    },

    {
      path: "/user/message",
      name: "user-readmessage",
      component: UserReadMessage,
    },

    {
      path: "/user/myprofile/:id",
      name: "user-myprofile",
      component: UserMyProfile,
    },

    {
      path: "/user/editprofile",
      name: "user-editprofile",
      component: UserEditProfile,
    },

    //
    // Routes for the guest
    //
    {
      path: "/search",
      name: "search",
      component: Search,
    },

    //
    // Routes for the host
    //
    {
      path: "/host/properties",
      name: "host-properties",
      component: HostManageProperties,
    },

    {
      path: "/host/addproperty",
      name: "host-addproperty",
      component: HostAddProperty,
    },

    {
      path: "/host/propertybookings/:id",
      name: "host-propertybookings",
      component: HostPropertyBookings,
    },

    {
      path: "/host/editproperty",
      name: "host-editproperty",
      component: HostEditProperty,
    },

    {
      path: "/host/propertypage/:id",
      name: "host-propertypage",
      component: HostPropertyPage,
    },

    {
      path: "/host/bookingdetails/:id",
      name: "host-bookingdetails",
      component: HostBookingDetails,
    },

    //
    // Routes for the renter
    //
    {
      path: "/renter/properties",
      name: "renter-properties",
      component: RenterManageProperties,
    },

    {
      path: "/renter/properties/recommended",
      name: "renter-recommended-properties",
      component: RenterRecommendedProperties,
    },

    {
      path: "/renter/editbooking",
      name: "renter-editbooking",
      component: RenterEditBooking,
    },

    {
      path: "/renter/bookingdetails/:id",
      name: "renter-bookingdetails",
      component: RenterBookingDetails,
    },

    {
      path: "/renter/bookingconfirmed",
      name: "renter-bookingconfirmed",
      component: RenterBookingConfirmed,
    },

    {
      path: "/renter/createbooking",
      name: "renter-createbooking",
      component: RenterCreateBooking,
    },

    //
    // Routes for the guest
    //

    //Home Page

    // -------------------------------------------------------------------------------------
    //                                  Template routes
    // -------------------------------------------------------------------------------------
    {
      path: "/",
      name: "presentation",
      component: PresentationView,
    },
    {
      path: "/pages/landing-pages/about-us",
      name: "about",
      component: AboutView,
    },
    {
      path: "/pages/landing-pages/contact-us",
      name: "contactus",
      component: ContactView,
    },
    {
      path: "/pages/landing-pages/author",
      name: "author",
      component: AuthorView,
    },
    {
      path: "/sections/page-sections/page-headers",
      name: "page-headers",
      component: PageHeaders,
    },
    {
      path: "/sections/page-sections/features",
      name: "page-features",
      component: PageFeatures,
    },
    {
      path: "/sections/navigation/navbars",
      name: "navigation-navbars",
      component: NavigationNavbars,
    },
    {
      path: "/sections/navigation/nav-tabs",
      name: "navigation-navtabs",
      component: NavigationNavTabs,
    },
    {
      path: "/sections/navigation/pagination",
      name: "navigation-pagination",
      component: NavigationPagination,
    },
    {
      path: "/sections/input-areas/inputs",
      name: "inputareas-inputs",
      component: InputAreasInputs,
    },
    {
      path: "/sections/input-areas/forms",
      name: "inputareas-forms",
      component: InputAreasForms,
    },
    {
      path: "/sections/attention-catchers/alerts",
      name: "ac-alerts",
      component: ACAlerts,
    },
    {
      path: "/sections/attention-catchers/modals",
      name: "ac-modals",
      component: ACModals,
    },
    {
      path: "/sections/attention-catchers/tooltips-popovers",
      name: "ac-tooltips-popovers",
      component: ACTooltipsPopovers,
    },
    {
      path: "/sections/elements/avatars",
      name: "el-avatars",
      component: ElAvatars,
    },
    {
      path: "/sections/elements/badges",
      name: "el-badges",
      component: ElBadges,
    },
    {
      path: "/sections/elements/breadcrumbs",
      name: "el-breadcrumbs",
      component: ElBreadcrumbs,
    },
    {
      path: "/sections/elements/buttons",
      name: "el-buttons",
      component: ElButtons,
    },
    {
      path: "/sections/elements/button-groups",
      name: "el-button-groups",
      component: ElButtonGroups,
    },
    {
      path: "/sections/elements/dropdowns",
      name: "el-dropdowns",
      component: ElDropdowns,
    },
    {
      path: "/sections/elements/progress-bars",
      name: "el-progress-bars",
      component: ElProgressBars,
    },
    {
      path: "/sections/elements/toggles",
      name: "el-toggles",
      component: ElToggles,
    },
    {
      path: "/sections/elements/typography",
      name: "el-typography",
      component: ElTypography,
    },
  ],
});

export default router;
